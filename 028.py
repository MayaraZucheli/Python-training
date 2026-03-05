from random import randint
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
jogador = int(input('Em qual número eu pensei? '))
computador = randint(0, 5)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Que pena! Vocie errou! Eu pensei no número {computador}')