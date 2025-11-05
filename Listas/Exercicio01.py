from math import inf

lista = []
maior = -inf
menor = inf   # já é positivo

for i in range(5):
    lista.append(int(input('Informe algum valor inteiro: ')))
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]
        
print(f'O maior valor da lista é: {maior}')
print(f'O menor valor da lista é: {menor}')

print(lista)
        
# Ver quem é o maior e o menor valor dentro da lista

# outro modo sem usar o -inf

# if i == 0 or lista[i] > maior:  (a primeira execução do i, sempre será == 0)
#    maior = lista[i]