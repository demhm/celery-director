"""Add workflows description, created_by

Revision ID: 9d563aaa548b
Revises: 05cf96d6fcae
Create Date: 2022-07-26 19:45:40.946254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9d563aaa548b"
down_revision = "05cf96d6fcae"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "workflows",
        sa.Column("description", sa.String(255), nullable=True),
    )
    sa.Column("password", sa.String(255), nullable=False),
    op.add_column(
        "workflows",
        sa.Column("created_by", sa.String(255), nullable=True),
    )


def downgrade():
    op.drop_column("workflows", "description")
    op.drop_column("workflows", "created_by")
