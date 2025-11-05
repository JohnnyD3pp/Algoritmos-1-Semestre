a = int(input('Informe um número A: '))
b = int(input('Informe um número B: '))
total = 0
total2 = 0

for i in range (1, a):
    if a % i == 0:
        total += i
for j in range (1, b):
    if b % j == 0:
        total2 += j
if total == b and total2 == a :
    print(f'Os divisores de {total} são = {a} e os divisores de {total2} são = {b} Eles são números amigos!')
else:
    print('Eles não são números amigos :(')