print("="*30)
print("Progama de PA")
print("="*30)
pt = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
cont = 10
while cont > 0:
    print(pt, "-> ", end="")
    pt += razao
    cont-=1
print("ACABOU!")