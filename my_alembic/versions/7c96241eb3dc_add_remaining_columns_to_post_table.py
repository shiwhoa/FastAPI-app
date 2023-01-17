"""add remaining columns to post table

Revision ID: 7c96241eb3dc
Revises: 8b92c957f64c
Create Date: 2023-01-16 20:37:26.020075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c96241eb3dc'
down_revision = '8b92c957f64c'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.add_column('posts',
    sa.Column('alembic_published', sa.Boolean(), nullable = False, server_default="TRUE"),
    )

    op.add_column('posts',
    sa.Column('alembic_created_at', sa.TIMESTAMP(timezone=True), server_default= sa.text('now()')),
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'alembic_published')
    op.drop_column('posts', 'alembic_created_at')
    pass
