class Animal():
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")

class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")

def main():
    cachorro = Cachorro(nome="Odie", idade=6)
    gato = Gato(nome="Garfield", idade=8)

    cachorro.emitir_som()
    gato.emitir_som()

if __name__ == '__main__':
    main()