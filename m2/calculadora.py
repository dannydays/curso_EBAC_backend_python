def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print(f"Erro: {ValueError}")

def menu_operacoes():
    print("\nEscolha uma operação: ")
    operacoes = ["Soma", "Subtração", "Multiplicação", "Divisão"]
    [print(f'{n} - {_}') for n,_ in enumerate(operacoes, start=1)]
    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    while True:
        num1 = obter_numero("Insira o primeiro número: ")
        num2 = obter_numero("Insira o segundo número: ")
        escolha = menu_operacoes()
        
        if escolha == '1':
            operacao = lambda a,b:a+b
            operacao_nome = "Soma"
        elif escolha == '2':
            operacao = lambda a,b:a-b
            operacao_nome = "Subtração"
        elif escolha == '3':
            operacao = lambda a,b:a*b
            operacao_nome = "Multiplicação"
        elif escolha == '4':
            while num2 == 0:
                print("Divisor não pode ser zero: ")
                num2 = obter_numero("Por favor, insira outro número para o divisor: ")
            operacao = lambda a,b:a/b
            operacao_nome = "Divisão"
        else:
            print("Opção inválida!")
            continue

        resultado = operacao(num1, num2)
        if resultado is None and operacao_nome == "Divisão":
            print(ZeroDivisionError)
        else:
            print(f"O resultado da {operacao_nome} é: {resultado}")

        while True:
            continuar = input("Deseja realizar outra operação? (S/N): ").strip().upper()
            if continuar == 'S':
                break
            if continuar == 'N':
                print("Encerrando...")
                quit()
            else:
                print("Opção inválida!")
                continue
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nEncerrando...")