def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print(f"Erro: {ValueError}")

def soma(x, y):
    return x+y

def subtracao(x, y):
    return x-y

def multiplicacao(x, y):
    return x*y

def divisao(x, y):
    return x/y

def menu_operacoes():
    print("\nEscolha uma operação: ")
    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
    for i, operacao in enumerate(operacoes, 1):
        print(f"{i} - {operacao}")
    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    while True:
        num1 = obter_numero("Insira o primeiro número: ")
        num2 = obter_numero("Insira o segundo número: ")
        escolha = menu_operacoes()

        if escolha == '1':
            operacao = soma
            operacao_nome = "Soma"
        elif escolha == '2':
            operacao = subtracao
            operacao_nome = "Subtração"
        elif escolha == '3':
            operacao = multiplicacao
            operacao_nome = "Multiplicação"
        elif escolha == '4':
            while num2 == 0:
                print("Divisor não pode ser zero: ")
                num2 = obter_numero("Por favor, insira outro número para o divisor: ")
            operacao = divisao
            operacao_nome = "Divisão"
        else:
            print("Opção inválida!")
            continue

        resultado = operacao(num1, num2)
        if resultado is None and operacao_nome == "Divisão":
            print(ZeroDivisionError)
        else:
            print(f"O resultado da {operacao_nome} é: {resultado}")
        
        continuar = input("Deseja realizar outra operação? (S/N): ").strip().upper()
        if continuar != 'S':
            print("Encerrando...")
            break

if __name__ == "__main__":
    main()