"""empty message

Revision ID: 14cf7f89b377
Revises: 82181db5b514
Create Date: 2021-04-02 06:35:27.404976

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '14cf7f89b377'
down_revision = '82181db5b514'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'province')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('province', mysql.VARCHAR(length=255), nullable=False))
    # ### end Alembic commands ###