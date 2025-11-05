# Versão tirando o if e else

n = int(input('Informe o valor de N: '))
y = 0
sinal = 1

if n <= 0:
    print('O valor de N deve ser maior que zero.')
else: 
    for denominador in range(1, n + 1):
        y += 1 / denominador * sinal
        sinal *= -1
    print(f'Y ={y: .2f}')

# Exercício 10