from math import sqrt

n = int(input('Informe um valor positivo: '))

total = 0
contador = 1

if n <= 0:
    print('Não leu dnv? 🖕🖕🖕') 
else:
    while contador <= n:
        total = total + contador / sqrt(contador)
        contador = contador + 1        
    print(f'{total}')