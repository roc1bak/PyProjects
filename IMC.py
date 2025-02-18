peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura (m)? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de', imc)

if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 18.6 <= imc < 25:
    print('Você está no peso ideal')
elif 25.1 <= imc < 30:
    print('Você está com sobrepeso')
elif 30.1 <= imc < 40:
    print('Você está obeso')
else:
    print('Você possui obesidade mórbida')
