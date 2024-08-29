from pydantic import BaseModel, Field, AnyHttpUrl, field_validator
from datetime import datetime

class UrlBase(BaseModel):
    original: str
    
    # @field_validator('url')
    # @classmethod
    # def validate_url(cls, v: str) -> str:
        
    
class UrlCreate(UrlBase):
    pass
    
class UrlUpdate(UrlBase):
    id: int
    
class UrlRead(UrlBase):
    short_code: str
    
class Url(UrlBase):
    id: int
    short_code: str
    visit_count: int = 0
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
