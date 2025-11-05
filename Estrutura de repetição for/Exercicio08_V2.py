valor = int(input('Informe um valor limite: '))

for i in range(1, valor + 1):
    # Encontra e soma os divisores de i
    soma_div_i = 0
    for j in range(1, i):
        if i % j == 0:
            soma_div_i += j
            
    # Encontra e soma os divisores da soma
    soma_div_soma = 0
    for j in range(1, soma_div_i):
        if soma_div_i % j == 0:
            soma_div_soma += j
            
    if i == soma_div_soma and i != soma_div_i:
        print(f'({i}, {soma_div_i})', end= ' ')