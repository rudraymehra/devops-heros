"""Add campus maintenance tables; preserve existing reference tasks on upgrade."""
from alembic import op
import sqlalchemy as sa

revision = "0002_campusfix"
down_revision = "0001_create_tasks"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "maintenance_requests",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("title", sa.String(200), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("location", sa.String(100), nullable=False),
        sa.Column("category", sa.String(30), nullable=False),
        sa.Column("urgency", sa.String(20), nullable=False),
        sa.Column("status", sa.String(30), nullable=False),
        sa.Column("reporter", sa.String(120), nullable=False),
        sa.Column("resolution", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_table(
        "request_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("request_id", sa.Integer(), sa.ForeignKey("maintenance_requests.id"), nullable=False),
        sa.Column("message", sa.String(250), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_request_events_request_id", "request_events", ["request_id"])


def downgrade():
    op.drop_index("ix_request_events_request_id", table_name="request_events")
    op.drop_table("request_events")
    op.drop_table("maintenance_requests")
