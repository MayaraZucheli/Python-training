from random import randint
print('Sou seu computador')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que vcoê consegue advinhar qual foi?')

pc = randint(0, 10)
tentativas = 1
palpite = int(input('Qual o seu palpite? '))
while palpite != pc:
    tentativas += 1
    if palpite < pc:
        print('Mais... Tente mais uma vez')
    else:
        print('Menos... Tente mais uma vez')
    
    palpite = int(input('Qual o seu palpite? '))
        
print(f'Acertou com {tentativas} tentativas. Parabéns!')
