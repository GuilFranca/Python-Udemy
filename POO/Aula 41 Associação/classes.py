class Escritor:
    def __init__(self,nome):
        self.__nome = nome
        self.__ferramenta = None
    
    # Getter
    @property
    def nome(self):
        return self.__nome
    
    # Getter
    @property
    def ferramenta(self):
        return self.__ferramenta

    # Setter
    @ferramenta.setter
    def ferramenta(self,valor_ferramenta):
        self.__ferramenta = valor_ferramenta

class Caneta:
    def __init__(self,marca):
        self.__marca = marca
    
    def escrever(self):
        print('Caneta está escrevendo...')
    
    # Getter
    @property
    def marca(self):
        return self.__marca

class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')