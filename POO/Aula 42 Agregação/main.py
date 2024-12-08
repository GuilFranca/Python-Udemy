from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
print(carrinho)

p1 = Produto('Camiseta',50)
p2 = Produto('Iphone',10000)
p3 = Produto('Caneca',15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produtos()
carrinho.soma_total()
print(carrinho.soma_total())