print("="*30)
print("Progama de PA")
print("="*30)
pt = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
for i in range(0, int(input("Digite a quantidade de termos da PA: "))):
    print(pt, "-> ", end="")
    pt += razao
print("ACABOU!")