n = float(input('Digite um valor: '))
v = int(n)
print(f'O valor digitado foi de {n} e a sua parte inteira é {v}')

# outra forma
from math import trunc
n = float(input('Digite um valor: '))
print(f'O valor digitado foi de {n} e a sua parte inteira é {trunc(n)}')