"""Adding agency_features JSON column to Agencies

Revision ID: 971f341c0204
Revises: 6ab8af7a1347
Create Date: 2017-05-25 15:19:51.722564

"""

# revision identifiers, used by Alembic.
revision = "971f341c0204"
down_revision = "6ab8af7a1347"

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "agencies",
        sa.Column(
            "agency_features", postgresql.JSON(astext_type=sa.Text()), nullable=True
        ),
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("agencies", "agency_features")
    ### end Alembic commands ###
