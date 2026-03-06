r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

sit_1 = ((r2 - r3) < r1 < (r2 + r3))
sit_2 = ((r1 - r3) < r2 < (r1 + r3))
sit_3 = ((r1 - r2) < r3 < (r1 + r2))

if (sit_1 and sit_2 and sit_3):
    print('Os segmentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima NÃO podem formar um triângulo.')