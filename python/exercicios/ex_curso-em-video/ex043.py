peso = float(input("informe seu peso: "))
altura = float(input("informe sua altura: "))
imc = peso / altura**2
print(" seu imc é: {:.1f}".format(imc))
if imc < 18.5:
    print("abaixo do peso")
elif 18.5 < imc <= 25:
    print("peso ideal")
elif 25 < imc <= 30:
    print("sobrepeso")
elif 30 < imc < 40:
    print("obesidade")
else:
    print("obesidade morbida")