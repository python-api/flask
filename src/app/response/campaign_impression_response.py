from marshmallow import fields, Schema


class CampaignImpressionResponse(Schema):
    id = fields.Integer(required=True)
    advertiser_id = fields.Integer(required=True)
    campaign_uuid = fields.String(required=True)
