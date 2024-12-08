from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('João')
print(escritor.nome)

caneta = Caneta('Bic')
print(caneta.marca)

maquina = MaquinaDeEscrever()
print(maquina)

print(escritor.nome)
print(caneta.marca)
print(maquina.escrever())

print(escritor.ferramenta)
escritor.ferramenta = caneta
escritor.ferramenta.escrever()


escritor.ferramenta = maquina
escritor.ferramenta.escrever()

# Não pode ser executado pois nome é um atributo privado
# escritor.nome = 'Jonas'
# print(escritor.nome)

# As outras instâncias funcionam normalmente mesmo sem a outra
del escritor
print(caneta.marca)
maquina.escrever()