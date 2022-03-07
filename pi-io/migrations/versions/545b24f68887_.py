"""empty message

Revision ID: 545b24f68887
Revises: d8d7b5f71046
Create Date: 2021-01-14 22:35:17.839126

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '545b24f68887'
down_revision = 'd8d7b5f71046'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_issue', sa.DATETIME(), nullable=True),
    sa.Column('config_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['config_id'], ['config.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('job')
    # ### end Alembic commands ###