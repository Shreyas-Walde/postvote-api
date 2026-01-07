"""add content column to post table

Revision ID: 34d7bbf3c370
Revises: 129a181d91c2
Create Date: 2026-01-07 13:16:32.867736

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34d7bbf3c370'
down_revision: Union[str, Sequence[str], None] = '129a181d91c2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# add column -> how to we undo that? 
def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

# drop the column -> solution (one step back)
def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
