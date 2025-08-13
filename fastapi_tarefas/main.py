from fastapi import FastAPI, HTTPException, Depends, status
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
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário ou senha inválidos", headers={"WWW-Authenticate": "Basic"})

tasks: list[Task] = []

# Rota para ler todas as tarefas
@app.get("/tasks/")
def get_tasks(page: int = 1, limit:int = 3, sort_by: str = "nome", credentials: HTTPBasicCredentials = Depends(authenticate)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Parâmetros inválidos: 'page' e 'limit' devem ser maiores que 0")
    
    if not tasks:
        return {"tasks": []}
    
    allowed_sort_fields = ["nome", "descricao", "concluida"]
    if sort_by not in allowed_sort_fields:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Campo de ordenação inválido. Use um dos seguintes: {', '.join(alowed_sort_fields)}")
    
    sorted_tasks = sorted(tasks, key=lambda x: getattr(x, sort_by))

    start = (page - 1) * limit
    end = start + limit

    paginated_tasks = [
        {"nome": task.nome, "descricao": task.descricao, "concluida": task.concluida}
        for task in sorted_tasks[start:end]
    ]

    return {"page": page, "limit": limit, "tasks": paginated_tasks}

# Rota para criar uma nova tarefa
@app.post("/tasks/")
def create_task(tarefa: Task, credentials: HTTPBasicCredentials = Depends(authenticate)):
    if any(existing_task.nome == tarefa.nome for existing_task in tasks):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tarefa já existe!")
    
    if not tarefa.nome or not tarefa.descricao:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nome e descrição são obrigatórios!")

    tasks.append(tarefa)

    return {"message": f"Tarefa '{tarefa.nome}' criada com sucesso!"}

# Rota para marcar uma tarefa como concluída
@app.put("/tasks/check/{nome}")
def check_task(nome: str, credentials: HTTPBasicCredentials = Depends(authenticate)):
    found_task = None
    for task in tasks:
        if task.nome == nome:
            found_task = task
            break

    if not found_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada!")

    found_task.concluida = True
    
    return {"message": f"Tarefa '{nome}' marcada como concluída!"}

# Rota para deletar uma tarefa
@app.delete("/tasks/{nome}")
def delete_task(nome: str, credentials: HTTPBasicCredentials = Depends(authenticate)):
    global tasks
    initial_tasks_count = len(tasks)
    tasks = [task for task in tasks if task.nome != nome]

    if len(tasks) == initial_tasks_count:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada!")
    
    return {"message": f"Tarefa '{nome}' deletada com sucesso!"}