valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe o segundo valor: '))
valor3 = int(input('Informe o terceiro valor: '))

if valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
    print(f'Seus valores devem ser diferentes.')
else:
    if valor1 < valor2 and valor1 < valor3:
        print(f'{valor1} é o menor')
    elif valor2 < valor3:
        print(f'{valor2} é o menor')
    else:
        print(f'{valor3} é o menor')