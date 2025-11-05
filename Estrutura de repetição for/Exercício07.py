inicio = int(input('Informe o início do intervalo: '))
fim = int(input('Informe o fim do intervalo: '))

for i in range (inicio, fim + 1):
    total = 0
    for divisao in range(1, i + 1):
        if i % divisao == 0:
            total += 1
    if total == 2:
        print(i, end=' ')
            
# Números primos entre o intervalo dado pelo user