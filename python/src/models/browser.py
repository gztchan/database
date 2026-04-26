from __future__ import annotations
from typing import TYPE_CHECKING

import uuid
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, func, text, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .profile import Profile
    from .browser_job import BrowserJob

class Browser(Base):
    __tablename__ = "Browser"
    __table_args__ = {"schema": "providence"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    profile_id: Mapped[uuid.UUID] = mapped_column(
        "profile_id",
        UUID(as_uuid=True),
        ForeignKey("providence.Profile.id"),
        nullable=False,
    )
    browser_job_id: Mapped[uuid.UUID] = mapped_column(
        "browser_job_id",
        UUID(as_uuid=True),
        ForeignKey("providence.BrowserJob.id"),
        nullable=True,
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    meta: Mapped[dict] = mapped_column(
        "metadata",
        JSONB,
        nullable=False,
        server_default=text("'{}'::jsonb"),
        default=dict,
    )

    browser_job: Mapped["BrowserJob"] = relationship(foreign_keys=[browser_job_id], back_populates="browser", cascade="all, delete-orphan", single_parent=True, lazy="noload")
    profile: Mapped["Profile"] = relationship(foreign_keys=[profile_id], back_populates="browser", lazy="noload")

    def __repr__(self):
        return f"""
    Browser(id={self.id},
    name={self.name},
    profile_id={self.profile_id},
    browser_job_id={self.browser_job_id},
    description={self.description},
    meta={self.meta}
    created_at={self.created_at}
    updated_at={self.updated_at}
    deleted_at={self.deleted_at}
"""
