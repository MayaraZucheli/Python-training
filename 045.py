import random
from time import sleep
print('Suas opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')

lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.randint(0, 2)
jog = int(input('Qual a sua jogada? '))

print(f'{" JO... ":*^20}')
sleep(1)
print(f'{" KEN... ":*^20}')
sleep(1)
print(f'{" PO... ":*^20}')

print(f'Computador jogou {lista[computador]}')
print(f'Jogador jogou {lista[jog]}')

if jog == computador:
    print(f'Empate!')
elif jog == 0 and computador == 1:
    print(f'Computador ganha!')
elif jog == 1 and computador == 0:
    print(f'Jogador ganha!')
elif jog == 2 and computador == 0:
    print(f'Computador ganha!')
elif jog == 0 and computador == 2:
    print(f'Jogador ganha!')
elif jog == 1 and computador == 2:
    print(f'Computador ganha!')
else:
    print('Insira valor válido')