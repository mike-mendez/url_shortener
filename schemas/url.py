from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl


class UrlBase(BaseModel):
    url: HttpUrl

    class config:
        orm_mode: True


class UrlCreate(UrlBase):
    short_code: str = None


class UrlUpdate(BaseModel):
    url: str | None = None


class UrlRead(UrlBase):
    id: int
    uuid: str
    short_code: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class UrlStats(UrlRead):
    visit_count: int
    active: bool
