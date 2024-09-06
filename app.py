import contextlib

from fastapi import FastAPI, status, Depends, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import RedirectResponse, JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_async_session
from .routers import urls
from .db import create_all_tables

from .helpers.endpoint import get_url_or_404
from .models.url import Url


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(urls.router)


# Exception handler
@app.exception_handler(RequestValidationError)
async def validation_exception(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST, content={"detail": "Invalid URL"}
    )


# Root
@app.get("/")
async def root():
    return {"message": "Let's shorten that URL!"}


# Redirect to original URL
@app.get("/{short_code}")
async def redirect_to_original(
    short_code: str,
    url: Url = Depends(get_url_or_404),
    session: AsyncSession = Depends(get_async_session),
) -> RedirectResponse:
    url.visit_count += 1
    session.add(url)
    await session.commit()

    # Must set status code to 301 here
    # Status code in decorator does not change default behaviors for redirects
    return RedirectResponse(url.url, status_code=status.HTTP_301_MOVED_PERMANENTLY)
