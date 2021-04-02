"""empty message

Revision ID: 05a8aa6c8ed0
Revises: 97129903d82d
Create Date: 2021-04-03 01:47:50.373032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05a8aa6c8ed0'
down_revision = '97129903d82d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('event', sa.Column('speaker', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('event', 'speaker')
    # ### end Alembic commands ###
