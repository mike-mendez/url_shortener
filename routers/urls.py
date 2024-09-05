from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import RedirectResponse

from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from ..db import get_async_session
from ..schemas.url import UrlCreate, UrlRead, UrlUpdate
from ..models.url import Url

router = APIRouter(
    prefix="/shorten",
    tags=["urls"],
)


async def pagination(skip: int = 0, limit: int = 10) -> tuple[int, int]:
    return (skip, limit)


async def get_url_or_404(
    short_code: str, session: AsyncSession = Depends(get_async_session)
) -> Url:
    select_query = select(Url).where(Url.short_code == short_code)
    result = await session.execute(select_query)
    # NOTE: scalar_one_or_none -> return a single object if it exists, or None otherwis
    url = result.scalar_one_or_none()

    if url is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return url


@router.get("/", response_model=list[UrlRead])
async def get_urls(
    pagination: tuple[int, int] = Depends(pagination),
    session: AsyncSession = Depends(get_async_session),
) -> Sequence[Url]:
    skip, limit = pagination
    select_query = select(Url).offset(skip).limit(limit)

    result = await session.execute(select_query)

    return result.scalars().all()


# Retrieve Original URL
@router.get("/{short_code}", response_model=UrlRead, status_code=status.HTTP_200_OK)
async def get_url(short_code: str, url: Url = Depends(get_url_or_404)) -> Url:
    return url


# Create Short URL
@router.post("/", response_model=UrlRead, status_code=status.HTTP_201_CREATED)
async def create_url(
    new_url: UrlCreate, session: AsyncSession = Depends(get_async_session)
) -> Url:
    url = Url(**new_url.model_dump())
    session.add(url)
    print(url)
    await session.commit()

    return url


@router.put("/{short_code}", response_model=UrlRead, status_code=status.HTTP_200_OK)
async def update_url(
    short_code: str,
    updated_url: UrlUpdate,
    url: Url = Depends(get_url_or_404),
    session: AsyncSession = Depends(get_async_session),
) -> Url:
    url_update_dict = updated_url.model_dump(exclude_unset=True)
    for key, value in url_update_dict.items():
        setattr(url, key, value)

    session.add(url)
    await session.commit()

    return url
