from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

tasks = []

# Rota para criar uma nova tarefa
@app.post("/tasks/")
def create_task(nome: str, descricao: str):
    if nome in [task["nome"] for task in tasks]:
        return HTMLResponse(content="Tarefa já existe!", status_code=400)

    tasks.append({
        "nome": nome,
        "descrição": descricao,
        "concluída": False
    })

    return HTMLResponse(content=f"Tarefa '{nome}' criada com sucesso!", status_code=201)

# Rota para ler todas as tarefas
@app.get("/tasks/")
def get_tasks():
    return HTMLResponse(content=json.dumps(tasks), status_code=200, media_type="application/json")

# Rota para marcar uma tarefa como concluída
@app.put("/tasks/check/{nome}")
def check_task(nome: str):
    if nome not in [task["nome"] for task in tasks]:
        return HTMLResponse(content="Tarefa não encontrada!", status_code=404)

    for task in tasks:
        if task["nome"] == nome:
            task["concluída"] = True
            break

    return HTMLResponse(content=f"Tarefa '{nome}' marcada como concluida!", status_code=200)

# Rota para deletar uma tarefa
@app.delete("/tasks/{nome}")
def delete_task(nome: str):
    if nome not in [task["nome"] for task in tasks]:
        return HTMLResponse(content="Tarefa não encontrada!", status_code=404)

    for task in tasks:
        if task["nome"] == nome:
            tasks.remove(task)
            break
    
    return HTMLResponse(content=f"Tarefa '{nome}' deletada com sucesso!", status_code=200)

