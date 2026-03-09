p = float(input('Qual o seu peso (kg): '))
a = float(input('Qual a sua altura (m): '))

imc = p / (a ** 2)

if imc < 18.5:
    print(f'Seu imc é de {imc:.2f}. Você está muito magro!')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu imc é de {imc:.2f}. Você está com peso ideal!')
elif imc > 24.9 and imc <= 29.9:
    print(f'Seu imc é de {imc:.2f}. Você está com sobrepeso!')
elif imc > 29.9 and imc <= 39.9:
    print(f'Seu imc é de {imc:.2f}. Você está com obesidade!')
else:
    print(f'Seu imc é de {imc:.2f}. Você está com obesidade grave!')
