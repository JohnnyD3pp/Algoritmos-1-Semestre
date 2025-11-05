from math import sqrt

a = float(input('Insira o valor de A (diferente de 0): '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))
delta = b ** 2 - 4 * a * c

if a == 0:
    print(f'O valor de A é inválido para a equação do 2° grau.')
elif delta < 0: 
    print(f'A equação não tem raiz real.')
else:
 x1 = (-b + sqrt(delta)) / ( 2 * a )
 x2 = (-b - sqrt(delta)) / ( 2 * a )
 
 print(f'x1 = {x1: .2f}')
 print(f'x2 = {x2: .2f}')