from pydantic import BaseModel, Field
from datetime import datetime

from ..helpers.generate_code import generate_code


class UrlBase(BaseModel):
    url: str

    class config:
        orm_mode: True


class UrlCreate(UrlBase):
    short_code: str = Field(default_factory=generate_code)


class UrlUpdate(BaseModel):
    url: str | None = None


class UrlRead(UrlBase):
    id: int
    uuid: str
    short_code: str
    visit_count: int = 0
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
