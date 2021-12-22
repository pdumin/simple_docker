from typing import Mapping
from fastapi import FastAPI

app = FastAPI()

@app.get('/home')
async def dictionary():
    return {
        "source" : 'home',
        "type" : 'another page'
    }

@app.get("/")
async def root():
    return {"message": "Hello World"}


