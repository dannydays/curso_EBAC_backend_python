opcoes = ['1', '2', '3', '4']

def inicio():
        print(
    '''Escolha uma operação:
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão''')

def fim():
    print('Encerrando calculadora... :)')

def main():
    while True:
        opcao = input('Digite a opção desejada:\n>>>')
        if opcao not in opcoes:
            print('Opção inválida!')
            continue
        n1 = float(input('Digite o primeiro número:\n>>>')) 
        n2 = float(input('Digite o segundo número:\n>>>'))

        if opcao == '1':
            print('Resultado: ', n1+n2)
        if opcao == '2':
            print('Resultado: ', n1-n2)
        if opcao == '3':
            print('Resultado: ', n1*n2)
        if opcao == '4':
            while n2 == 0:
                n2 = float(input('Divisor não pode ser zero:\n>>>'))
            print('Resultado: ', n1/n2)

        denovo = bool(int(input(
'''Deseja realizar mais uma operação?
1 - Sim
0 - Não
>>>''')))
        if not denovo:
            break
        inicio()

if __name__ == '__main__':
    inicio()
    main()
    fim()