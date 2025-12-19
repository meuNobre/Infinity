class Animal:
    def falar(self):
        print("Este animal faz um som genérico.")


class Cachorro:
    def falar(self):
        print("O cachorro está latindo.")


class Gato:
    def falar(self):
        print("O gato está miando.")


# ciar oss objetos
animal = Animal()
cachorro = Cachorro()
gato = Gato()

# chamada dos métodos
animal.falar()
cachorro.falar()
gato.falar()
