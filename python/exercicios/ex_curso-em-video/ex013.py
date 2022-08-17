valor = float(input("Digite o valor do salario: R$"))
desconto = 0.15
print("O salario de R${} com o reajuste de {:.0f}% vai para R${}".format(valor, desconto*100, valor+valor*desconto))