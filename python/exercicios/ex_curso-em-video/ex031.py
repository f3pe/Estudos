viagem = int(input("Qual a distancia que gostaria de viajar: "))
if viagem > 200:
    preco = viagem * 0.45
    print("O valor da viagem é R${:.2f}".format(preco))
else:
    preco = viagem * 0.50
    print("O valor da viagem é R${:.2f}".format(preco))