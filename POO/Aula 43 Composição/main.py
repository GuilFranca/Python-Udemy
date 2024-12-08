# Composição - Relação mais forte entre classes, uma classe vai ser dona de objetos de outra classe.
# Se apagar a classe principal, apaga todas as outras.

from classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente1.insere_endereco('Chique Chique', 'BA')
print(cliente1.nome)
cliente1.lista_enderecos()
# Quando o objeto principal é apagado os outros também são
del cliente1
print()

cliente2 = Cliente('Maria', 25)
cliente2.insere_endereco('Águas Lindas', 'GO')
print(cliente2.nome)
cliente2.lista_enderecos()

print()

print('#########################################################')
# Após o fim do código é tudo apagado