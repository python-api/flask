from marshmallow import fields, Schema


class CampaignImpressionResponse(Schema):
    campaign_uuid = fields.String()
