n = int(input('Informe o valor de N: '))
y = 0

if n <= 0:
    print('O valor de N deve ser maior que zero.')
else: 
    for denominador in range(1, n + 1):
        if denominador % 2 != 0:
            y += 1 / denominador
        else:
            y -= 1 / denominador
    print(f'Y:{y: .2f}')

# Exercício 10