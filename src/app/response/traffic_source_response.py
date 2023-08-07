from marshmallow import Schema, fields

class TrafficSourceResponse(Schema):
    id = fields.Integer(required=True)
    # name = fields.String(required=True)
    # is_archived = fields.Boolean(required=True)
    # is_postback_url = fields.Boolean(required=True)
    # postback_url = fields.String(required=True)
    # is_pixel_redirect_url = fields.Boolean(required=True)
    # pixel_redirect_url = fields.String(required=True)
    # partner_id = fields.Integer(required=True)
    # template_id = fields.Integer(required=True)
    # cost_currency_id = fields.Integer(required=True)
    # created_at = fields.DateTime(required=True)