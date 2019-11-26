from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel
import requests
import json
import re
import os


class Task(BaseModel):
    title: str
    description: str

app = FastAPI()

ip = os.getenv('toOhioIP')
print(ip)
@app.get("/")
async def root():
    return {"msg": "Hello World"}

@app.get("/healthcheck/")
async def healthcheck():
    a = requests.get(url = 'http://' + ip +':8000/healthcheck')
    return a.status_code

@app.get("/task/")
async def get_tasks():
    a = requests.get(url = 'http://' + ip +':8000/task')
    return a.json()

@app.post("/task/")
async def post_task(task: Task):
    data = {
        "title": task.title, 
        "description": task.description}
    requests.post(url = 'http://' + ip +':8000/task', data = data)

@app.get("/task/{id}")
async def get_task(id: int):
    a = requests.get(url = 'http://' + ip +':8000/task/' + id)
    return a.json()

@app.put("/task/{id}")
async def put_task(id: int, task: Task):
    data = {
        "title": task.title, 
        "description": task.description}
    a = requests.put(url = 'http://' + ip +':8000/task/' + id, data = data)
    return a.json()

@app.delete("/task/{id}")
async def delete_task(id: int):
    a = requests.delete(url = 'http://' + ip +':8000/task/' + id)
    return a.json()