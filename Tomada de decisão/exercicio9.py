valor1 = int(input('Insira o primeiro valor: '))
valor2 = int(input('Insira o segundo valor: '))
valor3 = int(input('Insira o tericeiro valor: '))

if valor1 > valor2:
    aux = valor1
    valor1 = valor2
    valor2 = aux
    
if valor1 > valor3:
    aux = valor1
    valor1 = valor3
    valor3 = aux
    
if valor2 > valor3:
    aux = valor2
    valor2 = valor3
    valor3 = aux
    
print(f'{valor1}{valor2}{valor3}')