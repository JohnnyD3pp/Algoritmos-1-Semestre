contador = 1
total = 1

fatorial = int(input('Informe um número inteiro e positivo: '))

while contador <= fatorial:
    total = total * contador
    contador = contador + 1
print(f'{fatorial}! {total}')

    
# Versão diminuindo o contador (6*5*4*3*2*1)

'''fatorial = int(input('Informe um número inteiro e positivo: '))

contador = fatorial
total = 1

while contador >= 1:
    total = total * contador
    contador = contador - 1
print(f'{total}')'''