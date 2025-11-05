tempo = float(input('Forneça o tempo gasto na viagem (horas) '))
velocidade = float(input('Forneça a velocidade média do carro (km) '))

litros = 10.5

gasto = (tempo * velocidade) / litros

print(f'seu consumo de gasolina foi de: {gasto: .4f}')