binario = int(input('Informe o valor em binário: '))
aux = binario
decimal = 0
expoente = 0

while binario > 0:
    digito = binario % 10
    decimal = decimal + digito * 2 ** expoente
    expoente += 1
    binario = binario // 10
    
print(f'{aux} --> {decimal}')