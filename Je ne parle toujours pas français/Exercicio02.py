n = int(input('Informe algum número: '))

maior = 0

for i in range(1, n + 1):
    total = 0
    
    for divisao in range(1, i + 1):
        if i % divisao == 0:
            total += 1
    if total == 2:
        if n % i == 0:
            if i > maior:
                maior = i
                
if maior > 0:
    print(f'O maior fator primo de {n} é: {maior}')
else:
    print('Esse número não tem fatores primos :(')
    
# Obs: o código demora um pouco pra processar