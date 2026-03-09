from datetime import date
nasc = int(input('Ano de nascimento: '))
print(f'Quem nasceu em {nasc} tem {date.today().year - nasc} anos em {date.today().year}.')
if date.today().year - nasc <= 18:
    print(f'Ainda faltam {18 - (date.today().year - nasc)} para o seu alistamento.')
    print(f'Seu alistamento será em {nasc + 18}.')
else:
    print(f'Você já deveria ter se alistado.')