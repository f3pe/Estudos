op = 0
while op != 5:
    print("""
    [1] - Somar
    [2] - Subtrair
    [3] - Multiplicar
    [4] - Dividir
    [5] - Sair
    """)
    op = int(input("Opção: "))
    if op == 1:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print("{} + {} = {}".format(n1, n2, n1+n2))
    elif op == 2:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print("{} - {} = {}".format(n1, n2, n1-n2))
    elif op == 3:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print("{} * {} = {}".format(n1, n2, n1*n2))
    elif op == 4:
        n1 = float(input("Digite o primeiro numero: "))
        n2 = float(input("Digite o segundo numero: "))
        print("{} / {} = {}".format(n1, n2, n1/n2))
    elif op == 5:
        print("Encerrando")
    else:
        print("Opção invalida")