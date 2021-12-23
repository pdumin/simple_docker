from typing import Mapping
from fastapi import FastAPI

app = FastAPI()

@app.get('/home_2')
async def dictionary():
    
    return {
        "source" : 'home_2',
        "type" : 'another page'
    }

@app.get('/home')
async def dictionary():

    return {
        "source" : 'home',
        "type" : 'another page'
    }

@app.get("/")
async def root():
    return {"message": "Hello World"}


