from fastapi import FastAPI, HTTPException

livros = {}

app = FastAPI()

app.title = "API de Livros"
app.description = "Uma API simples para gerenciar livros."
app.version = "1.0.0"

# Rota para obter todos os livros
@app.get("/livros")
def listar_livros():
    if not livros:
        raise HTTPException(status_code=404, detail="Nenhum livro encontrado.")
    return livros

# Rota para obter um livro específico
@app.get("/livros/{livro_id}")
def obter_livro(livro_id: int):
    livro = livros.get(livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return livro

# Rota para adicionar um novo livro
@app.post("/livros")
def adicionar_livro(nome: str, autor: str, ano: int):
    novo_id = max(livros.keys()) + 1 if livros else 1
    livros[novo_id] = {"nome": nome, "autor": autor, "ano": ano}
    return {"id": novo_id, "nome": nome, "autor": autor, "ano": ano}

# Rota para atualizar um livro existente
@app.put("/livros/{livro_id}")
def atualizar_livro(livro_id: int, nome: str = None, autor: str = None, ano: int = None):
    livro = livros.get(livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")

    if nome:
        livro["nome"] = nome
    if autor:
        livro["autor"] = autor
    if ano:
        livro["ano"] = ano
    
    return livro

# Rota para deletar um livro
@app.delete("/livros/{livro_id}")
def deletar_livro(livro_id: int):
    livro = livros.pop(livro_id, None)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return {"detail": "Livro deletado com sucesso."}