from math import sqrt

lista = []

# Laço para preencher o vetor

for i in range(5): # percorre todos os elementos um por um
    lista.append(int(input('Informe um valor positivo: ')))
    if lista[i] <= 0:
        print('0 ou um número negativo são valores inválidos')
        break
    
# Laço para imprimir os números primos

for numero in lista: # acessa diretamente os elementos dentro da lista
    n_div = 0
    for i in range(2, int(sqrt(numero)) + 1):
        if numero % i == 0:
            break
    else:
        print(numero, end=' ')
    