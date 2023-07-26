from fastapi import FastAPI, status
import asyncio
from aiohttp import ClientSession
from pydantic import BaseModel, Field


app = FastAPI()
task = None


class Request(BaseModel):
    cadastral_number: str = Field(pattern="^\d{1,2}:\d{1,2}:\d{5,11}:\d{1,4}$")
    latitude: str = Field(pattern="^\d{1,2}\.\d{1,7}$")
    longitude: str = Field(pattern="^\d{1,2}\.\d{1,7}$")


async def send_request(request):

    async with ClientSession() as session:
        url = 'http://server:8001/query'
        params = {
                "cad_num": request.cadastral_number,
                "ltd": request.latitude,
                "lgd": request.longitude
        }

        async with session.post(url=url, json=params) as response:
            answer = await response.json()
            return answer['message']


@app.post('/query')
async def query(request: Request):
    global task
    loop = asyncio.get_event_loop()

    if task in asyncio.all_tasks():
        return {"message": "try leater, task in process"}

    if not task or task.done():
        task = loop.create_task(send_request(request))

    return {"message": "request has been sent"}


@app.get('/result')
async def result():
    global task

    if task:
        if task.done():
            return {"result": task.result()}

        return {"message": "task in process"}

    return {"message": "wait request"}


@app.get('/ping')
async def ping():
    return status.HTTP_200_OK
