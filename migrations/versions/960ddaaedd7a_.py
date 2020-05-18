"""empty message

Revision ID: 960ddaaedd7a
Revises: a7df08ad4b96
Create Date: 2020-05-18 14:26:21.185121

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '960ddaaedd7a'
down_revision = 'a7df08ad4b96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_games_all_tournament_game_id_tournament_games', 'games_all', type_='foreignkey')
    op.drop_column('games_all', 'tournament_game_id')
    op.add_column('tournament_stage_rounds', sa.Column('name_', sa.String(length=50), nullable=True))
    op.drop_column('tournament_stage_rounds', 'name')
    op.add_column('tournament_stage_rounds_x01', sa.Column('type_', sa.Integer(), nullable=True))
    op.drop_column('tournament_stage_rounds_x01', 'type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tournament_stage_rounds_x01', sa.Column('type', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('tournament_stage_rounds_x01', 'type_')
    op.add_column('tournament_stage_rounds', sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.drop_column('tournament_stage_rounds', 'name_')
    op.add_column('games_all', sa.Column('tournament_game_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('fk_games_all_tournament_game_id_tournament_games', 'games_all', 'tournament_games', ['tournament_game_id'], ['id'])
    # ### end Alembic commands ###
