from datetime import date
ano = int(input('Ano do nascimento: '))
idade = date.today().year - ano
print(f'O atleta tem {idade}')

if idade <= 10:
    print('Classificação: MIRIM')
elif idade >= 10 and idade <= 18:
    print('Classificação: JUNIOR')
else:
    print('Classificação: ADULTO')

