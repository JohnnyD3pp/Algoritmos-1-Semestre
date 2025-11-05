# Programa para ler dois valores dados pelo user
# O Programa deverá imprimir os números entre o primeiro e o segundo.

contador = int(input('Informe o primeiro valor: '))
contador2 = int(input('Informe o último valor: '))

while contador <= contador2:
    print(f'{contador}')
    contador = contador + 1