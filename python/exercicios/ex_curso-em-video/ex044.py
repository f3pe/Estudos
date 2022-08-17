produto = float(input("Digite o preço do produto: "))
print("""
Selecione a opção de pagamento
[1] - A vista no dinheiro/cheque
[2] - A vista no cartão
[3] - Em 2x sem juros no cartão
[4] - em 3x ou mais no cartão
""")
op = input("Opção: ")
if op == '1':
    produto = produto - (produto * 0.1)
    print("O preço do produto será R${:.2f}".format(produto))
elif op == '2':
    produto = produto - (produto * 0.05)
    print("O preço do produto será R${:.2f}".format(produto))
elif op == '3':
    print("O preço do produto é R${:.2f} e cada parcela será no valor de R${:.2f}".format(produto, produto/2))
elif op == '4':
    produto = produto + (produto * 0.2)
    parcelas = int(input("em quantas parcelas sera o pagamento: "))
    print("Cada parcela será no valor de R${:.2f} e o valor total do produto será {}".format(produto/parcelas, produto))
else:
    print("opção invalida!")