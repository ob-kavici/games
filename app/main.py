from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Welcome to ob-kavici/games Microservice API!"}