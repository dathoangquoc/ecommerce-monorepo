from fastapi import FastAPI, APIRouter

from catalog_service import catalog


app = FastAPI()

api_router = APIRouter()
api_router.include_router(catalog.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
