inicio = int(input('Informe o início do intervalo: '))
fim = int(input('Informe o fim desse intervalo: '))

qtd_pft = 0

for i in range(inicio, fim + 1):
    if inicio > fim:
        print('O início do intervalo deve ser menor do que o fim.')
        break
    
    soma = 0
    
    for divisao in range(1, i):
        
        if i % divisao == 0:
            soma += divisao
            
    if soma == i:
        qtd_pft += 1
     
print(f'{qtd_pft}')