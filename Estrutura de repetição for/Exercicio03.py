qtd = int(input('Informe a quantidade de produtos comprados:'))
total = 0

for contador in range(1, qtd + 1):
    preco = float(input('Informe o preço do produto: '))
    total += preco # mesma coisa que total = total + valor

print('Digite 1 para o pagamento à vista')
print('Digite 2 para o pagamento parcelado (em 2 vezes)')
digito = int(input())

if digito == 1:
    total *= 0.9
    print(f'Valor a ser pago com 10% de desconto:{total: .2f}')
elif digito == 2:
    total *= 1.155
    parcela = total / 2
    print(f'O valor a ser pago em duas vezes é de:{parcela: .2f} por parcela.')
else:
    print('Forma de pagamento inválida.')

# Exercício 09