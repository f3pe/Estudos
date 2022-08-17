from math import hypot
n1 = float(input("Digite o tamanho do cateto adjacente: "))
n2 = float(input("Digite o tamanho do cateto oposto: "))
print("A hipotenusa desses catetos é {:.2f} ".format(hypot(n1, n2)))
