# Variação do exercício 1

contador = 1
maior = float('-inf')
# inf (infinito) -inf menor número infinito 
# inf (maior/menor número suportado pelo python no sistema operacional windows)

while contador <= 3:
    valor = int(input('Informe um número: '))
    if contador == 1 or valor > maior:
        maior = valor
    contador = contador + 1
print(f'O maior valor é: {maior}')