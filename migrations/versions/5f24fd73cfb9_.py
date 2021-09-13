"""Modified password hash length in database

Revision ID: 5f24fd73cfb9
Revises: c4910f0d7660
Create Date: 2021-09-13 14:19:56.957189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f24fd73cfb9'
down_revision = 'c4910f0d7660'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('student', 'password_hash', type_=sa.String(length=256))
    op.alter_column('lecturer', 'password_hash', type_=sa.String(length=256))
    op.alter_column('admin', 'password_hash', type_=sa.String(length=256))
    op.alter_column('superadmin', 'password_hash', type_=sa.String(length=256))


def downgrade():
    pass
