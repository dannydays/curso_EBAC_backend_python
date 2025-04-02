biblioteca = dict()
emprestimos = []

def input_nome():
    global biblioteca
    nome = input("Nome do livro: ")
    if nome not in biblioteca:
        return (False, nome)
    return (True, nome)

def adicionar_livro(biblioteca):
    while True:
        existe,nome = input_nome()
        if existe:
            print("erro: Livro já cadastrado.")
            continue
        break
    while True:
        try:
            qtd_exemplares = int(input("Quantidade de exemplares: "))
            break
        except ValueError:
            print("erro: Precisa ser número.")
            continue
    nome_autor = input("Nome do autor: ")
    biblioteca[nome] = {"Quantidade de exemplares": qtd_exemplares, "Nome do autor": nome_autor}
    print(f"Livro '{nome}' adicionado com sucesso!")

def listar_livros(biblioteca):
    if not biblioteca:
        print("\nSem livros!\n")
        return
    print("\nLista de Livros:\n")
    for livro in sorted(biblioteca):
        print("nome - quantidade - autor")
        print(f"{livro} - {biblioteca[livro]['Quantidade de exemplares']} - {biblioteca[livro]['Nome do autor']}")
        print('')

def remover_livro(biblioteca):
    while True:
        existe, nome = input_nome()
        if not existe:
            print(f"Livro não encontrado. Opções: {[_ for _ in biblioteca]}")
            continue
        break

    biblioteca.pop(nome)
    print(f"Livro {nome} removido com sucesso!")

def atualizar_quantidade(biblioteca, nome:str = None, nova_quantidade:int=None):
    if nova_quantidade:
        biblioteca[nome]["Quantidade de exemplares"] = nova_quantidade
        return

    while True:
        existe, nome = input_nome()
        if not existe:
            print(f"Livro não encontrado. Opções: {[_ for _ in biblioteca]}")
            continue
        break

    while True:
        try:
            nova_qtd = int(input(f"\nNova quantidade de exemplares para {nome}: "))
            break
        except ValueError:
            print("erro: Precisa ser número.")
            continue
    
    biblioteca[nome]["Quantidade de exemplares"] = nova_qtd
    print(f"\nQuantidade do livro '{nome}' atualizada para {nova_qtd} com sucesso!")

def registrar_emprestimo(biblioteca: dict, emprestimos: list):
    while True:
        existe, nome = input_nome()
        if not existe:
            print(f"Livro não encontrado. Opções: {[_ for _ in biblioteca]}")
            continue
        break

    while True:
        try:
            qtd_emprestimo = int(input(f"Quantidade de exemplares: "))
            break
        except ValueError:
            print("erro: Precisa ser número.")
            continue
    if qtd_emprestimo <= biblioteca[nome]["Quantidade de exemplares"]:
        atualizar_quantidade(biblioteca, nome, biblioteca[nome]["Quantidade de exemplares"] - qtd_emprestimo)
        
        emprestimos.append({"Título do livro": nome, "Quantidade emprestada": qtd_emprestimo})
    else:
        print("erro: Quantidade de empréstimo indisponível.")

def exibir_historico_emprestimo(emprestimos):
    [print(emp) for emp in emprestimos]

def menu():
    print('''Escolha uma opção:

    1 - Adicionar livro
    2 - Listar livros
    3 - Remover livro
    4 - Atualizar quantidade
    5 - Registrar empréstimo
    6 - Exibir histórico de empréstimos
    7 - Sair
''')

opcoes = {'1': (adicionar_livro, 1),
          '2': (listar_livros, 1),
          '3': (remover_livro, 1),
          '4': (atualizar_quantidade, 1),
          '5': (registrar_emprestimo, 2),
          '6': (exibir_historico_emprestimo, 1)}

def main():
    while True:
        menu()
        opcao = input(">>> ")
        if opcao == '7':
            print("Saindo...")
            break
        if opcao not in opcoes:
            print("Opção inválida!")
            continue
        funcao, n_args = opcoes[opcao]
        if n_args == 1:
            if opcao == '6':
                funcao(emprestimos)
            else:
                funcao(biblioteca)
        elif n_args == 2:
            funcao(biblioteca, emprestimos)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")