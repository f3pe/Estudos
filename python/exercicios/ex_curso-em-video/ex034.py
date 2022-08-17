salario = float(input("Digite o salario: "))
if salario > 1250.00:
    almento = salario + (salario * 0.1)
    print("Quem ganhva R${:.2f} agora vai ganhar R${:.2f}".format(salario, almento))
else:
    almento = salario + (salario * 0.15)
    print("Quem ganhva R${:.2f} agora vai ganhar R${:.2f}".format(salario, almento))