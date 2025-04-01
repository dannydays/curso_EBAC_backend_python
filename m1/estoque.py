import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

estoque = dict()

def adicionar_produto():
    nome = input("Nome do produto:\n>>>")
    
    if nome in estoque:
        print("Produto já existe")
        return
    try:
        quantidade = int(input("Quantidade:\n>>>"))
        if quantidade < 0:
            clear()
            print("Erro: A quantidade deve ser positiva.\n")
            return
    except ValueError:
        clear()
        print("Erro: Apenas números para quantidade\n")
        return
    try:
        preco = float(input("Preço:\n>>>"))
        if preco < 0:
            clear()
            print("Erro: O preço deve ser positivo.\n")
            return
    except ValueError:
        clear()
        print("Erro: Apenas números para preço\n")
        return
    produto = {
        'quantidade': quantidade,
        'preco': preco
    }
    estoque.update({nome:produto})
    clear()
    print(f"Produto {nome} adicionado com sucesso\n")

def listar_produtos():
    if not estoque:
        print('Sem produtos no estoque!\n')
        return
    
    produtos = sorted(list(estoque))
    print('Lista de produtos em estoque:')
    for produto in produtos:   
        print(f'\n  {produto}: {estoque[produto]["quantidade"]} - R${estoque[produto]["preco"]:.2f}')
    print('')

def remover_produto():
    if not estoque:
        print('Sem produtos no estoque!\n')
        return
    produtos = list(estoque)
    nome = input(f"Nome do produto: Opções:{list(produtos)}\n>>>")
    if nome not in estoque:
        clear()
        print(f"Produto não encontrado!\n")
        return
    estoque.pop(nome)
    clear()
    print(f"Produto {nome} removido com sucesso\n")

def atualizar_quantidade_produto():
    if not estoque:
        print('Sem produtos no estoque!\n')
        return
    produtos = list(estoque)
    nome = input(f"Nome do produto: Opções:{list(produtos)}\n>>>")
    if nome not in estoque:
        print(f"Produto {nome} não encontrado.")
        return
    quantidade = input("Nova quantidade:\n>>>")
    try:
        quantidade = int(quantidade)
        if quantidade < 0:
            print("\nErro: A quantidade deve ser positiva.\n")
            return
    except ValueError:
        print("erro: Apenas números para quantidade")
        return

    estoque[nome]['quantidade'] = quantidade
    clear()
    print(f"Quantidade do produto {nome} atualizada para {quantidade} com sucesso\n")

def main():
    opcoes = {
        '1': adicionar_produto,
        '2': listar_produtos,
        '3': remover_produto,
        '4': atualizar_quantidade_produto
    }

    while True:
        print(
'''Selecione uma opção:

    1 - Adicionar produto
    2 - Listar produtos
    3 - Remover produto
    4 - Atualizar quantidade de produto
    5 - Sair
''')
        opcao = input(">>>")

        if opcao == '5':
            print("Saindo...")
            break

        funcao = opcoes.get(opcao)
        if funcao:
            clear()
            funcao()
        else:
            clear()
            print("Opção inválida!\n")

if __name__ == "__main__":
    try:
        clear()
        main()
    except KeyboardInterrupt:
        print("\nSaindo...")