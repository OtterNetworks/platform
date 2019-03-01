"""create_users_table

Revision ID: 32b4550775f3
Revises: 7c4d47596f8f
Create Date: 2019-02-28 19:09:29.516983

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32b4550775f3'
down_revision = '7c4d47596f8f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )


def downgrade():
    op.drop_table('user')
