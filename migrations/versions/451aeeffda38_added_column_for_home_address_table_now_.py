"""Added column for home address. Table now stable.

Revision ID: 451aeeffda38
Revises: 207c6f5a3122
Create Date: 2021-09-10 13:39:41.644381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '451aeeffda38'
down_revision = '207c6f5a3122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('home_address', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('students', 'home_address')
    # ### end Alembic commands ###