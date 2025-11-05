n = int(input('Informe um número inteiro e positivo: '))
n_divisores = 0

if n <= 0:
    print('INTEIRO E POSITIVO 🖕')
else:
    for contador in range (1, n + 1):
        if n % contador == 0:
            n_divisores += 1
    if n_divisores == 2:
        print(f'{n} É um número primo!')
    else:
        print('Não é um número primo.')
        
# Exercício 08