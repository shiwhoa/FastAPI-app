"""add user table

Revision ID: 45249c044a2a
Revises: 679292e105ea
Create Date: 2023-01-16 20:18:29.871551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45249c044a2a'
down_revision = '679292e105ea'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('alembic_user_id', sa.Integer(), nullable = False),
    sa.Column('alembic_user_email', sa.String(), nullable = False),
    sa.Column('alembic_user_password', sa.String(), nullable = False),
    sa.Column('alembic_user_created_at', sa.TIMESTAMP(timezone=True), server_default= sa.text('now()'), nullable = False),
    sa.PrimaryKeyConstraint('alembic_user_id'),
    sa.UniqueConstraint('alembic_user_email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
