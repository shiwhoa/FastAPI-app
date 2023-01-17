"""add content column to post table

Revision ID: 679292e105ea
Revises: 67cf585627e2
Create Date: 2023-01-16 20:13:40.112234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '679292e105ea'
down_revision = '67cf585627e2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
    sa.Column('alembic_content', sa.Integer(), nullable = False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'alembic_content')

    pass
