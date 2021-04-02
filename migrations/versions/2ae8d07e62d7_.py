"""empty message

Revision ID: 2ae8d07e62d7
Revises: 14cf7f89b377
Create Date: 2021-04-02 07:20:25.130807

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2ae8d07e62d7'
down_revision = '14cf7f89b377'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registered_date', sa.DateTime(), nullable=False))
    op.drop_column('user', 'registeredDate')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('registeredDate', mysql.DATETIME(), nullable=False))
    op.drop_column('user', 'registered_date')
    # ### end Alembic commands ###