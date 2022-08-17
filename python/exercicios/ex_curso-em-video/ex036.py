casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o salario mensal do cliente: "))
anos = float(input("Em quantos anos será pago: "))
prestação = casa / (anos*12)
print("A prestação será de R${:.2f}".format(prestação))
if prestação > salario * 0.3:
    print("O salario não é compativel, emprestimo negado")
else:
    print("Emprestimo aprovado")

