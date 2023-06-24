from flask import Blueprint, request, g
from marshmallow import ValidationError
from werkzeug.exceptions import Unauthorized, Forbidden, HTTPException


class RequireAuthorizeBlueprint(Blueprint):
    def __init__(self, *args, allow_roles=[], denied_roles=[], allow_expired=[], **kwargs):
        pass