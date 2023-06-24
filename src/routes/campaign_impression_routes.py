from flask import Blueprint

from src.app.controllers import CampaignImpressionController

campaign_impression_router = Blueprint('campaign_impression_router', __name__, url_prefix='/')

@campaign_impression_router.route('/campaign_impression', methods=['POST'])
def list_campaign_impression():
    return CampaignImpressionController().list_campaign_impression()