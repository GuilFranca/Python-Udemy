from pessoa import Pessoa

p1 = Pessoa('Guilherme',20)
p2 = Pessoa('João', 32)

p1.falar('POO')
p2.falar('Mario')

p1.parar_falar()

p1.comer('Churras')
p2.comer('Sorvete')

# print(p2.get_ano_nascimento())
p2.get_ano_nascimento()
print(p2.ano_atual)