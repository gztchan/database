from __future__ import annotations

from typing import TYPE_CHECKING

from datetime import datetime
import uuid
from sqlalchemy import DateTime, Text, func, text, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .browser import Browser

class Profile(Base):
    __tablename__ = "Profile"
    __table_args__ = {"schema": "providence"}

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
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

    browser: Mapped["Browser"] = relationship(back_populates="profile", lazy="noload")

    def __repr__(self):
        return f"""
    Profile(id={self.id},
    name={self.name},
    description={self.description},
    metadata={self.metadata},
    created_at={self.created_at}
    updated_at={self.updated_at}
    deleted_at={self.deleted_at}
"""