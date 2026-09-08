from alembic import op
import sqlalchemy as sa

revision = "20260908_0002"
down_revision = "20251026_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "items",
        sa.Column("description", sa.String(length=500), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("items", "description")
