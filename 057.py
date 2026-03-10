s = input('Informe seu sexo [M/F]: ').upper().strip()
while s not in 'MF':
    s = input('Dados Invalidos. Por favor, informe o seu sexo: ').upper().strip()

print('Sexo registrado com sucesso!')
