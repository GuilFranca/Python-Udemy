from pessoa import Pessoa

# Criação de Objeto a partir da class Pessoa()
p1 = Pessoa('Luiz',29)
# p2 = Pessoa()

# Criação de variável presente somente dentro do objeto p1
p1.nome = 'Luiz'
p1.idade = 29

# print(nome) não funciona, pois não é uma variável global
# print(p2.nome) não funciona, pois não é uma variável global
print(p1.nome)
print()

# Utilizar a função/método
p1.falar()

# São objetos diferentes
print(p1)
# print(p2)

