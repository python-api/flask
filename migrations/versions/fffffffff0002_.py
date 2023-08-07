"""empty message

Revision ID: 40b0a9110025
Revises: 0577750d56d2
Create Date: 2023-08-07 15:45:30.886463

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'fffffffff0002'
down_revision = 'fffffffff0001'
branch_labels = None
depends_on = None


def upgrade():
    op.execute('TRUNCATE TABLE public.campaign_request_log')
    # Seeder database


def downgrade():
    pass