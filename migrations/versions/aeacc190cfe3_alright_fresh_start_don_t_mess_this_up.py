"""Alright. Fresh start. Don't mess this up.

Revision ID: aeacc190cfe3
Revises: 
Create Date: 2021-09-16 12:04:56.270676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aeacc190cfe3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('acc_role', sa.String(length=10), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('middle_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.CHAR(length=1), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('marital_status', sa.String(length=15), nullable=True),
    sa.Column('home_address', sa.String(length=128), nullable=True),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('position', sa.String(length=20), nullable=True),
    sa.Column('creation_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('lecturer',
    sa.Column('acc_role', sa.String(length=10), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('middle_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.CHAR(length=1), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('marital_status', sa.String(length=15), nullable=True),
    sa.Column('home_address', sa.String(length=128), nullable=True),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('student',
    sa.Column('acc_role', sa.String(length=10), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('middle_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.CHAR(length=1), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('marital_status', sa.String(length=15), nullable=True),
    sa.Column('home_address', sa.String(length=128), nullable=True),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('superadmin',
    sa.Column('acc_role', sa.String(length=10), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('middle_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.CHAR(length=1), nullable=True),
    sa.Column('dob', sa.Date(), nullable=True),
    sa.Column('marital_status', sa.String(length=15), nullable=True),
    sa.Column('home_address', sa.String(length=128), nullable=True),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=256), nullable=True),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('position', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('superadmin')
    op.drop_table('student')
    op.drop_table('lecturer')
    op.drop_table('admin')
    # ### end Alembic commands ###
