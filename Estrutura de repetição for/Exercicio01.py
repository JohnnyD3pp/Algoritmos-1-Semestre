n = int(input('Informe um número inteiro e positivo: '))

if n <= 0:
    print('O valor DEVE SER INTEIRO E POSITIVO 🖕')
else:
    for contador in range (-n, n + 1):
        if contador != 0 and n % contador == 0:
            print(f'{contador}')
            
# Exercício 07