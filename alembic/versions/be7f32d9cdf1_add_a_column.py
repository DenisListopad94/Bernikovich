"""Add a column

Revision ID: be7f32d9cdf1
Revises: e0ea64d357e3
Create Date: 2024-04-02 21:15:27.441491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be7f32d9cdf1'
down_revision: Union[str, None] = 'e0ea64d357e3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
