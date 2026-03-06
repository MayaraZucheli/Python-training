sal = float(input('Qual o seu salário? R$'))
if sal >= 1250:
    print(f'Seu salário com aumento de 10% é R${sal * 0.10 + sal:.2f}')
else:
    print(f'Seu salário com aumento de 10% é R${sal * 0.15 + sal:.2f}')
