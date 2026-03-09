from datetime import date
total_maior = 0
total_menor = 0
atual = date.today().year

for i in range(1, 4):
    nasc = int(input(f'Em que ano a {i} pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1

print(f'Ao todo tivemos {total_maior} pessoa é maior de idade')
print(f'Ao todo tivemos {total_menor} pessoa é menor de idade')








