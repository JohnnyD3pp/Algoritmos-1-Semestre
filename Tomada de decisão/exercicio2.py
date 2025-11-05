prova1 = float(input('Digite a nota da prova 1: '))
prova2 = float(input('Digite a nota da prova 2: '))
trab1 = float(input('Digite a nota do trabalho 1: '))
trab2 = float(input('Digite a nota do trabalho 2: '))

media = prova1 * 70 + prova2 * 70 + trab1 * 30 + trab2 * 30

nota = media / 200

if nota >= 7:
    print(f'Aprovado! Sua média é: {nota}')
else:
    print(f'Reprovado. Sua média é: {nota}')    
