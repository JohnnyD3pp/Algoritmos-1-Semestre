# Programa para imprimir números pares entre os valores que o user digitou

contador = int(input('Informe o valor inicial: '))
contador2 = int(input('Informe o valor final: '))

while contador <= contador2:
    if contador % 2 == 0:
        print(f'{contador}')
    contador = contador + 1