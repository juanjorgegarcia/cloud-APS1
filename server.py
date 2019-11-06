from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Task(BaseModel):
    title: str
    description: str

t = Task(**{'title':'titulo', 'description': 'descricao'})
d = {0: t}

@app.get("/healthcheck")
def healthcheck():
    return 200

@app.post("/task")
async def create_task(task: Task, task_id: int):
    try:
        d[task_id] = task
        return f'Task ->Title: {task.title}, Description: {task.description} foi adicionada na tabela task'
    except:
        return f'Não posso inserir {task.title, task.description} na tabela task'

@app.get("/task")
async def get_tasks():
    try:
        return d
    except:
        return f'Não posso inserir {task.title, task.description} na tabela task'

@app.get("/items/{task_id}")
async def read_item(task_id: int):
    try:
        return d[task_id]
    except:
        return f'Não existe nenhuma task com o id {task_id} na tabela task'

@app.delete("/task/{task_id}")
async def delete_task(task_id: int):
    try:
        del d[task_id]
        return f'Task ->task_id: {task_id} foi removida na tabela task'
    except:
        return f'Não posso remover a task com o id: {task_id} na tabela task'


@app.put("/task")
async def update_task(task: Task):
    try:
        d[task_id] = Task(**{'title':task.title, 'description': task.description})
        return f"Task alterado para: {task} com sucesso"
    except:
        return f'Não posso alterar a task para: {task}'


