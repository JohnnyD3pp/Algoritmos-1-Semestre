qtd = int(input('Informe a quantidade de triângulos: '))
nmr_triangulo = 0

for contagem in range(1, qtd + 1):
    
    nmr_triangulo += 1
    print(f'-------- Triângulo {nmr_triangulo} --------')
    
    lado1 = int(input('Informe a medida do primeiro lado: '))
    lado2 = int(input('Informe a medida do segundo lado: '))
    lado3 = int(input('Informe a medida do terceiro lado: '))
    
    
    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        break
    
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
        if lado1 == lado2 and lado1 == lado3 and lado3 == lado2:
            print('O seu triângulo é um equilátero!')
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print('O seu triângulo é um isósceles!')
        else:
            print('O seu triângulo é um escaleno!')
    else:
        print('Os valores não formam um triângulo.')
        
# Exercício 11