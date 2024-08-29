from fastapi import APIRouter, HTTPException, status, Response
from fastapi.responses import RedirectResponse
from ..db import db
from ..schemas.url import Url, UrlCreate, UrlRead
from ..helpers.random_key import generate_random_key

router = APIRouter(
    prefix="/shorten",
    tags=["urls"],
)

# @router.get("/")
async def read_urls():
    return db

# Retrieve Original URL
@router.get("/{shortened_url}")
async def read_url(shortened_url: str) -> Url:
    for url in db.urls.values():
        if url.short_code == shortened_url:
            return url
    raise HTTPException(status_code=404, detail="URL not found")




# Create Short URL
@router.post("/", status_code=201)
async def create_url(request: UrlCreate) -> None:
    id = max(db.urls.keys() or (0,)) + 1 # tuple (0,) ensures at least one value is passed to max
    url = Url(id=id, original=request.original, short_code=generate_random_key())
    db.urls[id] = url
    return url
