from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
print(carrinho)

p1 = Produto('Camiseta',50)
p2 = Produto('Iphone',10000)
p3 = Produto('Caneca',15)

carrinho.inserir_produto(p1)