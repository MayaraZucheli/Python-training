casa = int(input('Valor da casa: R$'))
sal = int(input('Salário do comprador: R$'))
fin = int(input('Quantos anos de financiamento? '))

prestacao = casa / (fin * 12)


if prestacao > (sal * 0.3):
    print(f'Para pagar uma casa de R${casa} em {fin} anos, a prestação será de R${prestacao:.2f}. Emprestimo negado!')
else: 
    print(f'Para pagar uma casa de R${casa} em {fin} anos, a prestação será de R${prestacao:.2f}. Emprestimo Aprovado!')