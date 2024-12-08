# Super classe
class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        # Mostra qual o nome do Molde/class
        self.nome_classe = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nome_classe} está falando...')

# subclasse
# Herdam atraves do parenteses
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome} está comprando...')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome} está estudando...')