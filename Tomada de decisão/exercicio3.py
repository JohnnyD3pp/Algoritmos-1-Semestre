from math import sqrt

p1x = int(input('Informe a coordenada x do ponto 1: '))
p1y = int(input('Informe a coordenada y do ponto 1: '))
p2x = int(input('Informe a coordenada x do ponto 2: '))
p2y = int(input('Informe a coordenada y do ponto 2: '))


distancia_p1 = sqrt(p1x ** 2 + p1y ** 2)
distancia_p2 = sqrt(p2x ** 2 + p2y ** 2)

print(f'distância do ponto 1 até a origem: {distancia_p1: .3f}')
print(f'distância do ponto 2 até a origem: {distancia_p2: .3f}')

if distancia_p1 < distancia_p2:
    print('O ponto 1 está mais próximo da origem')
else:
    ('O Ponto 2 está mais próximo da origem')