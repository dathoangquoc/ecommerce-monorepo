from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter

from src.auth.router import router as auth_router
from src.catalog.router import router as catalog_router
from src.db.utils import init_db, seed_data



@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    await seed_data()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(catalog_router)


@app.get("/")
async def read_root():
    return "Hello from FastAPI"

