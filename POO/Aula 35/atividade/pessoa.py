from datetime import datetime

class Pessoa:
    # Variável da class em si
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        self.comendo = False
        self.falando = False
    
    def comer(self,alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} está falando no momento.')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            # return interrompe a execução do método atual.
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self,assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar, pois está de boca cheia.')
            return
        
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        
        print(f'{self.nome} parou de falar.')
        self.falando = False
    
    def get_ano_nascimento(self):
        # return self.ano_atual - self.idade
        print(f'O ano de nascimento de {self.nome} é {self.ano_atual - self.idade}')
