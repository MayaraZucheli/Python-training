nome = input('Digite seu nome completo: ').strip().upper()
print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome.split()[0]}')
print(f'Seu ultimo nome é {nome.split()[-1]}')

# outra forma
nome = input('Digite seu nome completo: ').strip().upper()
n = nome.split()
print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {n[0]}')
print(f'Seu ultimo nome é {n[-1]}')

