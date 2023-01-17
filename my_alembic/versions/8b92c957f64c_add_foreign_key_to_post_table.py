"""add foreign key to post table

Revision ID: 8b92c957f64c
Revises: 45249c044a2a
Create Date: 2023-01-16 20:28:26.347838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b92c957f64c'
down_revision = '45249c044a2a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
    sa.Column('alembic_user_id', sa.Integer(), nullable = False))

    op.create_foreign_key('posts_users_fk',
    source_table="posts",
    referent_table="users",
    local_cols=['alembic_user_id'],
    remote_cols=['alembic_user_id'],
    ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table = 'posts')
    op.drop_column('posts', 'alembic_user_id')
    pass
