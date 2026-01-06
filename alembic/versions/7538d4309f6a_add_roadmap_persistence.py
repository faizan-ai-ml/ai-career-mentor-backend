"""add_roadmap_persistence

Revision ID: 7538d4309f6a
Revises: 28e95fb25eb9
Create Date: 2025-12-16 02:38:15.260323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7538d4309f6a'
down_revision: Union[str, None] = '28e95fb25eb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
