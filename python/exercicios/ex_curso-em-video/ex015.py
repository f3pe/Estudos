dias = int(input("Digite por quantos dias o carro foi alugado: "))
km = float(input("Digite quantos quilometros foram rodados: "))
valor = km*0.15 + dias*60
print("O valor a ser pago é R${:.2f}".format(valor))