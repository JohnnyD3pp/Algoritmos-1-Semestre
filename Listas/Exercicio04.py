produto = []
estoque = []
preco = []

qtd = int(input('Quantidade de produtos: '))

# Entrada de dados de cada produto

for i in range(qtd):
    print(f'Produto {i + 1}')
    
    produto.append(input('Nome do produto: '))
    estoque.append(int(input('Quantidade em estoque: ')))
    preco.append(float(input('Preço do produto: ')))