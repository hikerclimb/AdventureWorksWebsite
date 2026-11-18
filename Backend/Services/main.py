from Repo.AccessRepo import AccessRepo
from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def root():
    AccessRepo()
