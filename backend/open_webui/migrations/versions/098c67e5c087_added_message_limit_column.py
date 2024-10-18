"""Added message limit column

Revision ID: 098c67e5c087
Revises: 6a39f3d8e55c
Create Date: 2024-10-18 16:13:33.291340

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import open_webui.apps.webui.internal.db
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision: str = '098c67e5c087'
down_revision: Union[str, None] = '6a39f3d8e55c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("user", sa.Column("message_limit", sa.BigInteger()))

def downgrade() -> None:
    op.drop_column("user", "message_limit")
