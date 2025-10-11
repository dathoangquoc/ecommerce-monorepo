from fastapi import FastAPI, APIRouter

from src.auth.router import router as auth_router
from src.catalog.router import router as catalog_router


app = FastAPI()

app.include_router(auth_router)
app.include_router(catalog_router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
