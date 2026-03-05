import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = math.hypot(oposto, adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')