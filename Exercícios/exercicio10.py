 # Entrada de dados
binario = int(input('Informe um npumero em binário com no máximo 4 bit --> '))
 
# Processamento de dados
bit1 = binario // 1000
bit2 = binario % 1000 // 100
bit3 = binario % 100 // 10
bit4 = binario % 10

decimal = bit4 * 1 + bit3 * 2 + bit2 * 4 + bit1 * 8

# Saída de dados
print(f'{binario} em decimal é {decimal}')