import json
import os
import sys
import traceback
import logging
import requests
from flask import request, g as this_request
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound, BadRequest, Unauthorized

from src import db
from src.config.constants import *
from src.config.error_codes import ErrorCode
from src.helpers import MakeResponse

# Create log
logger = logging.getLogger()
logger.setLevel(logging.ERROR)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class ExceptionHandler:
    def __init__(self) -> None:
        self.make_response = MakeResponse
    def error_handler(self, function):
        def handle(*args):
            try:
                return function(*args)
            except ValidationError as validation_err:
                db.session.rollback()
                return self.make_response.failure(validation_err.messages), 400
            except BadRequest as ex:
                db.session.rollback()
                return self.make_response.failure(ex.description), 400
            except NotFound as ex:
                db.session.rollback()
                return self.make_response.failure(ex.description), 404
            except Exception as ex:
                logger.error(ex, exc_info=True)
                sendMessageToSlack(msg=str(ex))
                db.session.rollback()
                env = os.getenv('APP_SETTINGS')
                if env == 'DEV' or env == 'LOCAL':
                    return self.make_response.failure({'unknown': ex.args}), 500
                else:
                    return self.make_response.failure({'unknown': ErrorCode.INTERNAL_SERVER_ERROR.message()}), 500
        return handle


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
