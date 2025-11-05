lista = []
total_par = 0

for i in range(5):
    lista.append(int(input('Informe um valor inteiro: ')))
    if lista[i] % 2 == 0:
        total_par += 1
    
portancetagem_par = total_par / len(lista) * 100

print(f'Porcentagem de números pares:{portancetagem_par: .2f}%')
print(f'Porcentagem de números ímpares:{100 - portancetagem_par: .2f}%')
# Exemplo 100 - 40% = 60%
