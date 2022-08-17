pt = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
cont = termos = 10
while cont != 0:    
    while cont > 0:
        print(pt, "-> ", end="")
        pt += razao
        cont-=1
    print("ACABOU!")
    cont = int(input("Quantos termos vc pretende monstrar a mais: "))
    termos += cont
print("A quantidade de termos exibidos foi {}".format(termos))