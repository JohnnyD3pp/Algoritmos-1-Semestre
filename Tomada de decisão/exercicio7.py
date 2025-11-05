base = float(input('Informe o valor da base do triângulo: '))
lado1 = float(input('Informe o valor da lateral esquerda do triângulo: '))
lado2 = float(input('Informe o valor da lateral direita do triângulo: '))

if base < lado1 + lado2 and lado1 < lado2 + base and lado2 < base + lado1:
    print(f'O seu valor representa um lado de um triângulo!')
else:
    print('Seu valor não pode representar o lado de um triângulo.')