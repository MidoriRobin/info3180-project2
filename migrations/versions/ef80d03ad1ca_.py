"""empty message

Revision ID: ef80d03ad1ca
Revises: 9f6c332c842d
Create Date: 2020-05-16 23:41:27.292033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef80d03ad1ca'
down_revision = '9f6c332c842d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('username', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'username')
    # ### end Alembic commands ###
