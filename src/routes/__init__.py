from flask import Blueprint

from src.routes.campaign_impression_routes import campaign_impression_router

version = Blueprint('v1', __name__)
report = Blueprint('report', __name__)

# Register sub blueprints here
version.register_blueprint(report, url_prefix='/report')

# Nesting Blueprints
report.register_blueprint(campaign_impression_router)