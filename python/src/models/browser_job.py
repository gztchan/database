import uuid
from datetime import datetime
from typing import TYPE_CHECKING
from sqlalchemy import DateTime, String, Text, func, text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .browser import Browser

class BrowserJob(Base):
    __tablename__ = "BrowserJob"
    __table_args__ = {"schema": "providence"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    status: Mapped[str] = mapped_column(String(32), index=True, default="pending")
    meta: Mapped[dict] = mapped_column(
        "metadata",
        JSONB,
        nullable=False,
        server_default=text("'{}'::jsonb"),
        default=dict,
    )

    browser: Mapped["Browser"] = relationship(back_populates="browser_job", lazy="noload")