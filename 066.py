n = int(input('Digite um número: '))
cont = 0
soma = 0
while True:
    if n == 999:
        break
    cont += 1
    soma += n
    n = int(input('Digite um número: '))
print(f'Você digitou {cont} número e a soma deles é de {soma}')