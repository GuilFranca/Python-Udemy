class A:
    # Variável de classe que está disponivel para todas as instancias
    vc = 123

    # def __init__(self):
        # variável de instância
        # self.vc = 321

a1 = A()
a2 = A()

A.vc = 'Alterado'
# criou um atributo para a instância a1
a1.vc = 321

# __dict__ mostra todos os atributos do objeto
print(a1.__dict__)

print(a2.__dict__)

print(A.__dict__)

print(a1.vc)
print(a2.vc)
print(A.vc)