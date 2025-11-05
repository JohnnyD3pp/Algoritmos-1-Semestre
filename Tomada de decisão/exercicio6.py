from math import sqrt

x = float(input('Insira o valor de x: '))

#if verifica se o valor de x é válido
if x > 5 or x < -5:
    y = (x - 8) / sqrt(x ** 2 - 25)
    print(f'O resultado é {y: .4f}')
else:
    print(f'Valor inválido para x')
