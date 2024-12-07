# É uma função que recebe dois argumentos
def mult(x, y):
    return x * y

# Criação do molde de Objeto
# Por convenção é utilizado o CamelCase.

# self se refere ao objeto em si associado ao molde
class Pessoa:
    # def __init__ é o construtor de uma class, responsável por inicalizar os atributos do molde
    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        # Quando for instanciado ira exibir o 'valor'
        variavel = 'valor'
        print(variavel)
        pass

    # Função dentro de class vira um método
    # A variável não está disponivel fora no init, já o self.alguma coisa está
    def outro_metodo(self):
        print(self.nome)
        print(variavel)

