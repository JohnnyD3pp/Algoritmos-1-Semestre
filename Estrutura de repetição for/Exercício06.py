n = int(input('Informe um número inteiro e positivo: '))


if n < 0:
    print('Informe um número inteiro e positivo.')
else:
    for linha in range(1, n + 1):
        for contador in range(1, linha + 1):
            print(contador, end= ' ')
        print()