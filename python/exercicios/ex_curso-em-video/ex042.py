print("-=-"*20)
print("Analisador de triangulos")
print("-=-"*20)
l1 = int(input("Digite o tamanho do primeiro seguimento: "))
l2 = int(input("Digite o tamanho do segundo seguimento: "))
l3 = int(input("Digite o tamanho do terceiro seguimento: "))

if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print("É possivel formar um trinagulo")
    if l1 == l2 == l3:
        print("E é um triangulo EQUILÀTERO")
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print("E é um trianulo ESÒSCELES")
    else:
        print("e é um tringulo ESCALENO")
else:
    print("Não é possivel formar um triangulo")