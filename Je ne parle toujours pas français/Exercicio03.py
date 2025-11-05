aluno = int(input('Informe a quantidade de alunos pesquisados: '))

favor = 0
contra = 0

for i in range(1, aluno + 1):
    voto = int(input('Você é a favor ou contra a criação da estação de bicicletas? A favor - 1 | Contra - 2 '))
    
    if voto > 2 or voto < 1:
        print('Por favor selecione uma das opções dadas.')
        
    match voto:
        case 1:
            favor += 1
        case 2:
            contra += 1
            
    porcent_favor = favor / aluno * 100
    
print(f'A porcentagem de votos a favor é de:{porcent_favor: .2f}%')
print(f'A porcentagem de votos contra é de:{100 - porcent_favor: .2f}%')
    