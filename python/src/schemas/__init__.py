from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class BrowserSchema(BaseModel):
    id: UUID
    profile_id: UUID
    browser_job_id: UUID | None = None
    name: str
    description: str | None = None
    metadata: dict = Field(alias="metadata_")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    profile: Optional["ProfileSchema"] = None
    browser_job: Optional["BrowserJobSchema"] = None

    model_config = {"from_attributes": True}

class BrowserJobSchema(BaseModel):
    id: UUID
    status: str
    metadata: dict = Field(alias="metadata_")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    model_config = {"from_attributes": True}


class Page(BaseModel):
    id: UUID
    browser_id: UUID
    target_id: str
    # status: str
    metadata: dict
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    model_config = {"from_attributes": True}


class ProfileSchema(BaseModel):
    id: UUID
    name: str
    description: str | None = None
    metadata: dict = Field(alias="metadata_")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    browser: Optional["BrowserSchema"] = None

    model_config = {"from_attributes": True}


BrowserSchema.model_rebuild()
ProfileSchema.model_rebuild()
BrowserJobSchema.model_rebuild()