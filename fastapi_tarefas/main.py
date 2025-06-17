from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json
from pydantic import BaseModel
from typing import Optional

class Task(BaseModel):
    nome: str
    descricao: str
    concluida: Optional[bool] = False

app = FastAPI()

tasks: list[Task] = []

# Rota para criar uma nova tarefa
@app.post("/tasks/")
def create_task(tarefa: Task):
    if any(existing_task.nome == tarefa.nome for existing_task in tasks):
        return HTMLResponse(content="Tarefa já existe!", status_code=400)

    tasks.append(tarefa)

    return HTMLResponse(content=f"Tarefa '{tarefa.nome}' criada com sucesso!", status_code=201)

# Rota para ler todas as tarefas
@app.get("/tasks/")
def get_tasks(): 
    return tasks

# Rota para marcar uma tarefa como concluída
@app.put("/tasks/check/{nome}")
def check_task(nome: str):
    found_task = None
    for task in tasks:
        if task.nome == nome:
            found_task = task
            break

    if not found_task:
        return HTMLResponse(content="Tarefa não encontrada!", status_code=404)

    found_task.concluida = True
    
    return HTMLResponse(content=f"Tarefa '{nome}' marcada como concluída!", status_code=200)

# Rota para deletar uma tarefa
@app.delete("/tasks/{nome}")
def delete_task(nome: str):
    global tasks
    initial_tasks_count = len(tasks)
    tasks = [task for task in tasks if task.nome != nome]

    if len(tasks) == initial_tasks_count:
        return HTMLResponse(content="Tarefa não encontrada!", status_code=404)
    
    return HTMLResponse(content=f"Tarefa '{nome}' deletada com sucesso!", status_code=200)