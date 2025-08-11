from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
load_dotenv()

class Task(BaseModel):
    nome: str
    descricao: str
    concluida: Optional[bool] = False

app = FastAPI()

username = os.getenv("USER")
password = os.getenv("PASS")

security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username == username and credentials.password == password:
        return True
    else:
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")

tasks: list[Task] = []

# Rota para ler todas as tarefas
@app.get("/tasks/")
def get_tasks(page: int = 1, limit:int = 3, credentials: HTTPBasicCredentials = Depends(authenticate)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="Parâmetros inválidos: 'page' e 'limit' devem ser maiores que 0")
    
    if not tasks:
        return HTMLResponse(content="Nenhuma tarefa encontrada!", status_code=404)
    
    start = (page - 1) * limit
    end = start + limit

    paginated_tasks = [
        {"nome": task.nome, "descricao": task.descricao, "concluida": task.concluida}
        for task in tasks[start:end]
    ]

    return {"page": page, "limit": limit, "tasks": paginated_tasks}

# Rota para criar uma nova tarefa
@app.post("/tasks/")
def create_task(tarefa: Task, credentials: HTTPBasicCredentials = Depends(authenticate)):
    if any(existing_task.nome == tarefa.nome for existing_task in tasks):
        return HTMLResponse(content="Tarefa já existe!", status_code=400)
    
    if not tarefa.nome or not tarefa.descricao:
        return HTMLResponse(content="Nome e descrição são obrigatórios!", status_code=400)

    tasks.append(tarefa)

    return HTMLResponse(content=f"Tarefa '{tarefa.nome}' criada com sucesso!", status_code=201)

# Rota para marcar uma tarefa como concluída
@app.put("/tasks/check/{nome}")
def check_task(nome: str, credentials: HTTPBasicCredentials = Depends(authenticate)):
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
def delete_task(nome: str, credentials: HTTPBasicCredentials = Depends(authenticate)):
    global tasks
    initial_tasks_count = len(tasks)
    tasks = [task for task in tasks if task.nome != nome]

    if len(tasks) == initial_tasks_count:
        return HTMLResponse(content="Tarefa não encontrada!", status_code=404)
    
    return HTMLResponse(content=f"Tarefa '{nome}' deletada com sucesso!", status_code=200)