from marshmallow import Schema, EXCLUDE, validate, fields, pre_load, ValidationError
from common.constants import DEFAULT_LIMIT, DEFAULT_PAGE, DEFAULT_SORT, SORT_ORDERS


class BaseRequest(Schema):
    class Meta:
        unknown = EXCLUDE

    @pre_load()
    def convert_string(self, data, **kwargs):
        if data is None:
            return {}
        data = dict(data)
        for key in data:
            if type(data[key]) is str:
                # Case default: return str trim
                data[key] = data[key].strip()
                # Case empty: return None
                if data[key] == '':
                    data[key] = None
        return data


class PaginationRequest(Schema):
    page = fields.Int(
        required=False,
        allow_none=True,
        load_default=DEFAULT_PAGE,
    )

    limit = fields.Int(
        allow_none=True,
        required=False,
        load_default=DEFAULT_LIMIT,
    )

    sort = fields.Str(
        allow_none=True,
        required=False,
        validate=validate.OneOf(SORT_ORDERS, error='c_c00'),
        load_default=DEFAULT_SORT,
    )
