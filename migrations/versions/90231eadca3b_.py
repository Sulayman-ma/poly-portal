"""empty message

Revision ID: 90231eadca3b
Revises: aeacc190cfe3
Create Date: 2021-09-16 15:04:35.420964

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.schema import Column


# revision identifiers, used by Alembic.
revision = '90231eadca3b'
down_revision = 'aeacc190cfe3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('student', Column(
        'active_status', type_=sa.Boolean, server_default=True
    ))
    op.add_column('lecturer', Column(
        'active_status', type_=sa.Boolean, server_default=True
    ))
    op.add_column('admin', Column(
        'active_status', type_=sa.Boolean, server_default=True
    ))
    op.add_column('superadmin', Column(
        'active_status', type_=sa.Boolean, server_default=True
    ))


def downgrade():
    op.drop_column('student', 'active_status')
    op.drop_column('lecturer', 'active_status')
    op.drop_column('admin', 'active_status')
    op.drop_column('superadmin', 'active_status')
