import json
import os
import sys
import traceback
import logging
import requests
from flask import request, g as this_request
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound, BadRequest, Unauthorized
from common.error_codes import ErrorCode
from common.make_response import MakeResponse
from database import db
from .constants import *
from flask_jwt_extended import (
    decode_token
)
from common.env_var import INTERNAL_API_KEY

# Create log
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Helpers:
    def get_current_user():
        identity = this_request.identity
        return {"id":identity.user_id, "role":identity.role}

    def error_handler(function):
        def handle(*args):
            try:
                return function(*args)
            except ValidationError as validation_err:
                db.session.rollback()
                return MakeResponse.failure(validation_err.messages), 400
            except BadRequest as ex:
                db.session.rollback()
                return MakeResponse.failure(ex.description), 400
            except NotFound as ex:
                db.session.rollback()
                return MakeResponse.failure(ex.description), 404
            except Exception as ex:
                logger.error(ex, exc_info=True)
                sendMessageToSlack(msg=str(ex))
                db.session.rollback()
                env = os.getenv('APP_SETTINGS')
                if env == 'DEV' or env == 'LOCAL':
                    return MakeResponse.failure({'unknown': ex.args}), 500
                else:
                    return MakeResponse.failure({'unknown': ErrorCode.internal_server_error.value}), 500
        return handle

    def handlePaginate(datas):
        page = datas.page
        totals = datas.total
        limit = datas.per_page
        pages = datas.pages
        return {
            'total_row': totals,
            'total_page': pages,
            'current_page': page,
            'limit': limit
        }

    def handle_paginate_condition(datas, total_page):
        page = datas.page
        totals = datas.total
        limit = datas.per_page
        pages = total_page
        return {
            'total_row': totals,
            'total_page': pages,
            'current_page': page,
            'limit': limit
        }

    def allowed_file(file_name):
        return '.' in file_name and \
               file_name.rsplit('.', 1)[1].lower() in allowed_extensions

    def get_file_type(file_name):
        c = os.path.splitext(file_name)[1]
        c = c.split('.')
        if len(c) > 1:
            return c[1]
        else:
            return None

    def is_image_file(file_name):
        type = Helpers.get_file_type(file_name)
        if type:
            return type.lower() in image_extensions
        return False

    def is_video_file(file_name):
        type = Helpers.get_file_type(file_name)
        if type:
            return type.lower() in video_extensions
        return False

    def is_gif_file(file_name):
        type = Helpers.get_file_type(file_name)
        if type:
            return type.lower() in gif_extensions
        return False

    def is_csv_file(file_name):
        type = Helpers.get_file_type(file_name)
        if type:
            return type.lower() in csv_extension
        return False

    def is_doc_file(file_name):
        type = Helpers.get_file_type(file_name)
        if type:
            return type.lower() in doc_extension
        return False

    def is_archive_file(file_name):
        type = Helpers.get_file_type(file_name)
        if type:
            return type.lower() in archive_extensions
        return False

    def validate_file_name(file_name):
        if type(file_name) is not str:
            raise ValidationError([ErrorCode.format_file_upload.message()])
        if not Helpers.allowed_file(file_name):
            raise ValidationError([ErrorCode.format_file_upload.message()])

    def invalid_limit_decimals(value: str, limit: int):
        if value[::-1].find('.') > limit:
            return True
        return False

    def find_first(iterable, default=None):
        for item in iterable:
            return item
        return default


def sendMessageToSlack(msg):
    env = os.getenv('APP_SETTINGS')
    if env != "LOCAL":
        hook = "https://hooks.slack.com/services/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"
        headers = {'content-type': 'application/json'}
        payload = {"attachments": [
            {
                "username": "API ERROR BOT",
                "icon_url": "https://cdn-icons-png.flaticon.com/512/2399/2399453.png",
                "fallback": msg,
                "pretext": "API Error!!!",
                "color": "#fff",
                "mrkdwn_in": ["text"],
                "text": f"**Error**: {msg}\n **URL**: {request.url}\n **Method**: {request.method}\n "
                        f"**Args**: {request.args}\n **IP Address**: {request.remote_addr} \n **ENV**: {env} \n"
                        f"**Tracing info**: {traceback.format_exc()}"
            }
        ]
        }

        r = requests.post(hook, data=json.dumps(payload), headers=headers)
