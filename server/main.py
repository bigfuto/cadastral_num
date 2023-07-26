from fastapi import FastAPI, status
from pydantic import BaseModel, Field
from random import randint
import time

app = FastAPI()


class Request(BaseModel):
    cad_num: str = Field(pattern="^\d{1,2}:\d{1,2}:\d{5,11}:\d{1,4}$")
    ltd: str = Field(pattern="^\d{1,2}\.\d{1,7}$")
    lgd: str = Field(pattern="^\d{1,2}\.\d{1,7}$")


@app.post('/query')
def index(request: Request):
    time.sleep(randint(0, 60))
    return {'message': bool(randint(0, 2))}


@app.get('/ping')
async def ping():
    return status.HTTP_200_OK