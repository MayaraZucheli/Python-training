nome = input('Em qual o seu nome completo? ').strip()
print(f'Seu nome tem Silva?')
if 'SILVA' in nome.upper():
    print(True)
else:
    print(False)