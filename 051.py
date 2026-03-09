print('Os 10 primeiros termos de uma PA')

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = termo + (11 - 1) * razao

for i in range(termo, pa, razao):
    print(i, end=' - ')
print('Acabou')