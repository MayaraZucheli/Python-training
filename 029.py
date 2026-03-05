vel = int(input('Qual é a velocidade atula do carro? '))
if vel > 80:
    print('Multado! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${(vel - 80) * 7:.2f}')
else:
    print('Tenha um bom dia! Dirija com segurança!')