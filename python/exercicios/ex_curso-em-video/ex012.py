valor = float(input("Digite o valor do produto: R$"))
desconto = 0.05
print("O produto que custa R${} com o desconto de {:.0f}% vai para R${}".format(valor, desconto*100, valor-valor*desconto))