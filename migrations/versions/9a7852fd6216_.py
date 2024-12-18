"""empty message

Revision ID: 9a7852fd6216
Revises: 
Create Date: 2024-12-04 16:23:06.201723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a7852fd6216'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('followerCount', sa.Integer(), nullable=False),
    sa.Column('followingCount', sa.Integer(), nullable=False),
    sa.Column('friendCount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
