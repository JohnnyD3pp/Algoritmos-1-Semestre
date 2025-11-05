# Programa que leia 5 números do usuário e fornece o maior

contador = 1
maior = 0
while contador <= 5:
    valor = int(input('Informe um número: '))
    if contador == 1 or valor > maior:
        maior = valor
    contador = contador + 1
print(f'O maior valor é: {maior}')