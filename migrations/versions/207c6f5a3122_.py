"""Alter reg number column manually as Alembic did not identify change

Revision ID: 207c6f5a3122
Revises: 3da06e95a45f
Create Date: 2021-09-10 13:28:19.607163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '207c6f5a3122'
down_revision = '3da06e95a45f'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('students', 'reg_number', nullable=False, existing_nullable=False, type_=sa.CHAR(length=9), existing_type=sa.String(32))


def downgrade():
    pass
