# entrada de dados
altura = float(input('Informe a altura do retângulo:'))
base = float(input('Informe a base do retângulo: '))

# processamento de dados
area = base * altura
perimetro = 2 * (altura + base)

# saída de dados
print(f'O valor da sua área é: {area: .3f}')
print(f'O valor do perimetro é: {perimetro: .3f}')