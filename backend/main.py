from fastapi import FastAPI

from models import *


app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'Hello world'}
