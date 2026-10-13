from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator

RequestStatus = Literal["REPORTED", "IN_PROGRESS", "RESOLVED"]
Category = Literal["ELECTRICAL", "PLUMBING", "NETWORK", "FURNITURE", "OTHER"]
Urgency = Literal["NORMAL", "URGENT"]


class RequestCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(default="", max_length=4000)
    location: str = Field(min_length=2, max_length=100)
    category: Category
    urgency: Urgency = "NORMAL"
    reporter: str = Field(min_length=2, max_length=120)


class RequestUpdate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")
    title: str | None = Field(default=None, min_length=3, max_length=200)
    description: str | None = Field(default=None, max_length=4000)
    location: str | None = Field(default=None, min_length=2, max_length=100)
    category: Category | None = None
    urgency: Urgency | None = None
    status: RequestStatus | None = None
    resolution: str | None = Field(default=None, max_length=4000)

    @model_validator(mode="after")
    def reject_explicit_null(self):
        # Omitted fields mean 'keep current'; null must not erase required data.
        if any(getattr(self, field) is None for field in self.model_fields_set):
            raise ValueError("Fields cannot be null; omit fields you do not want to update")
        return self


class RequestOut(RequestCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    status: RequestStatus
    resolution: str
    created_at: datetime
    updated_at: datetime


class EventOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    request_id: int
    message: str
    created_at: datetime
