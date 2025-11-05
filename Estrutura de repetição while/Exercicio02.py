# Programa que pega o valor dado pelo usuário e mostra sua tabuada até 10
# Após a tabuada o programa deve perguntar se o usuário quer imprimir outra tabuada

resposta = 'sim'
while resposta == 'sim':
    nmr = int(input('Informe um número inteiro: '))
    contador = 0
    
    while contador <= 10:
        resultado = nmr * contador 
        print(f'{nmr} * {contador} = {resultado}')
        contador = contador + 1
        
    resposta = input(f'Deseja imprimir outra tabuada? (sim ou não) ')
