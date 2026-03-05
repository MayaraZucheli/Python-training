import math
a = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'O seno é: {s:.2f}, cosseno é: {c:.2f} e a tangente é: {t:.2f}.')