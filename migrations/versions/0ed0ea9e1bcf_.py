"""empty message

Revision ID: 0ed0ea9e1bcf
Revises: ef80d03ad1ca
Create Date: 2020-05-17 00:25:43.068807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ed0ea9e1bcf'
down_revision = 'ef80d03ad1ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
