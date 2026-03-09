p = float(input('Preço da compras: R$'))
dinheiro = int(1)
vista = int(2)
duas_vezes = int(3)
tres_vezes = int(4)
print('[ 1 ] a vista dinheiro/cheque: 10% de desconto')
print('[ 2 ] a vista cartão: 5% de desconto')
print('[ 3 ] 2x no cartão: 2% de juros')
print('[ 4 ] 3x ou mais no cartão: 3% de juros')
op = int(input('Qual sua opção? '))
if op == 1:
    print(f'Sua compra de R${p} vai custar R${p - (p * 0.10)} ')
elif op == 2:
    print(f'Sua compra de R${p} vai custar R${p - (p * 0.05)} ')
elif op == 3:
    print(f'Sua compra de R${p} vai custar R${p + (p * 0.02)} ')
elif op == 4:
    print(f'Sua compra de R${p} vai custar R${p + (p * 0.03)} ')
else:
    print('Insira uma opção válida')
