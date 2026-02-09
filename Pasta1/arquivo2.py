import os
os.system('cls')
massa = float(input('Indique seu peso em Kg: '))
altura = float(input('Indique sua altura em metros: '))
imc = massa / altura ** 2
print(f'Seu IMC é: {imc:.2f}')



if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você tem o peso ideal.')
elif 25 <= imc < 30:
    print('Você apresenta excesso de peso.')
elif 30 <= imc < 35:
    print('Você apresenta obesidade tipo I.')
elif 35 <= imc < 40:
    print('Você apresenta obesidade tipo II.')
elif imc >= 40:
    print('Você apresenta obesidade tipo III.')

