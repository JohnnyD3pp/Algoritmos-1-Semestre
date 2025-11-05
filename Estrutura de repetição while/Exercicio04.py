denominador = 1
y = 0

n = int(input('Informe um número positivo: '))

if n <= 0:
    print(f'Sabe ler não jumento... 🖕🖕🖕')
else:
    while denominador <= n:
        y = y + 1 / denominador
        denominador = denominador + 1
    print(f'O resultado é: {y: .3f}')