"""empty message

Revision ID: 128bdbddde78
Revises: 0f8102f27175
Create Date: 2020-04-03 16:37:31.096964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '128bdbddde78'
down_revision = '0f8102f27175'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('backer_until', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('is_backer', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_backer')
    op.drop_column('users', 'backer_until')
    # ### end Alembic commands ###
