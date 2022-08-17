velocidade = float(input("Digite a velocidade do carro: "))
if(velocidade > 80):
    print("Você passou do limite de velocidade de 80Km/h")
    multa = (velocidade - 80) * 7
    print("Você deverá pagar uma multa de R${:.2f}".format(multa))
print("Tenha um bom dia e ditija com segurança!")