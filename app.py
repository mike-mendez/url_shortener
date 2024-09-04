import contextlib
from fastapi import FastAPI
from .routers import urls
from .db import create_all_tables


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
    await create_all_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(urls.router)


@app.get("/")
async def root():
    return {"message": "Let's shorten that URL!"}
