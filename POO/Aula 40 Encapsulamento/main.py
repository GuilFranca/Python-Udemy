# Encapsulamento serve para esconder determinadas partes do seu código, para proteger sua aplicação/classe/método.

"""
Programação Orientada a Objeto Clássica
public, protected, private

Python
_ Private para a comunidade
__ Private para o código

ATRIBUTO
self.dados = {} - Público
self._dados = {} - Protected (public _)
self.__dados = {} - Private (INSTÂNCIA_NOMECLASSE__NOMEATRIBUTO)

MÉTODO
def inserir_clientes():
def _inserir_clientes():
def __inserir_clientes():
"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}
    
    # Para poder chamar self.dados mesmo sendo privado
    # @property
    # def dados(self):
    #     return self.__dados
    
    def inserir_cliente(self,id,nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id : nome}
        else:
            self.__dados['clientes'].update({id:nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id,nome)

    def apaga_cliente(self,id):
        del self.__dados['clientes'][id]



bd = BaseDeDados()
bd.inserir_cliente(1,'Otávio')
bd.inserir_cliente(2,'Miranda')
bd.inserir_cliente(3,'Rose')
print(bd.__dict__)
# Não é acessado fora da classe
# print(bd.__dados)

bd.apaga_cliente(2)
bd.lista_clientes()

# Cria um novo atributo com o mesmo nome do atributo privado
bd.__dados = 'Uma outra coisa'
print(bd.__dados)
bd.lista_clientes()

# Atributo privador original
# instância._classe__atributoPrivado
print(bd._BaseDeDados__dados)

# @property
# print(bd.dados)
# db.dados = 'Outra coisa' / Não pode
