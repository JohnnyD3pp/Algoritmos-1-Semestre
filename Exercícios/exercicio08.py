# Entrada de dados
numero = int(input('Informe um número entre 100 e 999: '))

# Processamento de dados
resultado = (numero % 100)
resultado2 = (resultado // 10)
#Ou numero // 10 % 10

# Saída de dados
input('Você acha que o mágico acertará o número do meio? ')
print(f'Seu número do meio é: {resultado2}')
input('Eai ele acertou? ')