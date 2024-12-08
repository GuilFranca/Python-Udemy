class Cliente:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = [] 

    def insere_endereco(self,cidade,estado):
        # Insere a instancia da class Endereco
        self.enderecos.append(Endereco(cidade,estado))
    
    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)
    
    # Função para quando o objeto é deletado
    def __del__(self):
        print(f'{self.nome} FOI APAGADO')

class Endereco:
    def __init__(self,cidade,estado):
        self.cidade = cidade
        self.estado = estado

    # Função para quando o objeto é deletado
    def __del__(self):
        print(f'{self.cidade}/{self.estado} FORAM APAGADOS')
