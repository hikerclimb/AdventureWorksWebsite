from Repo.AccessRepo import AccessRepo
from fastapi import FastAPI

app = FastAPI()


@app.get("/test/{emailAddress}")
async def root(emailAddress: str):
    print('enter root')
    accessRepo =  AccessRepo()
    user = accessRepo.selectUser(emailAddress)
    print('exit root', user)
    return user
    
