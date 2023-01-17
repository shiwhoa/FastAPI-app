"""create posts table

Revision ID: 67cf585627e2
Revises: 
Create Date: 2023-01-16 19:59:26.161329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67cf585627e2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
    sa.Column('alembic_id', sa.Integer(), nullable = False, primary_key=True),
    sa.Column('alembic_title', sa.String(), nullable = False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
