# Entrada de dados
numero = int(input('Informe um número entre 100 e 999: '))

# Processamento de dados
resultado = numero % 10
resultado2 = numero // 10 % 10
resultado3 = numero // 100

unidade = resultado * 100
dezena = resultado2 * 10
centena = resultado3 * 1

valor = unidade + dezena + centena

# Saída de dados
print(f'Seu resultado é: {valor}')