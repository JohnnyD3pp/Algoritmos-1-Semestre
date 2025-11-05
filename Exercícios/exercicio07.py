# importação da função sqrt da biblioteca math
from math import sqrt

# entrada de dados
x = float(input('Informe o valor de X: '))

# processamento de dados
y = sqrt(1 + ((x ** 4 - 1) / (2 * x ** 2)) ** 2) - (x ** 2) / 2

# saída de dados
print(f'y = {y: .3f}')