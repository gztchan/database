from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class BrowserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    profile_id: UUID
    browser_job_id: UUID | None = None
    name: str
    description: str | None = None
    metadata: dict = Field(default_factory=dict, alias="meta")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    profile: Optional["ProfileSchema"] = None
    browser_job: Optional["BrowserJobSchema"] = None

class BrowserJobSchema(BaseModel):
    id: UUID
    status: str
    metadata: dict = Field(default_factory=dict, alias="meta")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    model_config = {"from_attributes": True}


class Page(BaseModel):
    id: UUID
    browser_id: UUID
    target_id: str
    # status: str
    metadata: dict = Field(default_factory=dict, alias="meta")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    model_config = {"from_attributes": True}


class ProfileSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    name: str
    description: str | None = None
    metadata: dict = Field(default_factory=dict, alias="meta")
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None

    browser: Optional["BrowserSchema"] = None


BrowserSchema.model_rebuild()
ProfileSchema.model_rebuild()
BrowserJobSchema.model_rebuild()