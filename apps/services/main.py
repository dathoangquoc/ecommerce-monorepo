from fastapi import FastAPI, APIRouter

from auth_service import auth
from catalog_service import catalog


app = FastAPI()

app.include_router(catalog.router)
app.include_router(auth.router)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
