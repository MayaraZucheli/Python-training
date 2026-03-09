tab = int(input('Digite um número para sua tabuada: '))

for count in range(1, 11):
    multi = count * tab
    print(f'{tab} X {count} = {multi}')
