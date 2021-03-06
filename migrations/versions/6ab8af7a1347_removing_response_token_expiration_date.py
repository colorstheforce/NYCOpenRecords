"""Removing Response Token Expiration Date

Revision ID: 6ab8af7a1347
Revises: 8797e9a71f62
Create Date: 2017-05-11 17:15:08.243557

"""

# revision identifiers, used by Alembic.
revision = "6ab8af7a1347"
down_revision = "8797e9a71f62"

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("response_tokens", "expiration_date")
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "response_tokens",
        sa.Column(
            "expiration_date",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
        ),
    )
    ### end Alembic commands ###
