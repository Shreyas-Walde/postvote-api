"""add foreign-key to posts table

Revision ID: ccc70161dc3a
Revises: 1e5113982c44
Create Date: 2026-01-07 13:43:05.500489

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ccc70161dc3a'
down_revision: Union[str, Sequence[str], None] = '1e5113982c44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('posts_users_fk',table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
