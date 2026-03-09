n = int(input('Digite um número: '))
total = 0

for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m', end=' ')
        total += 1
    else:
        print('\033[m', end=' ')
    print(f'{i}', end=' ')
        
    
print(f'\n\033[m O número {n} foi divisível {total} vezes')

if total == 2:
    print(f'{n} é PRIMO')
else:
    print(f'{n} NÃO é PRIMO')
