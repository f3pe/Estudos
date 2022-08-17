#sequencia de fibonacci
n1 = 0
n2 = 1
cont = int(input("Quantos termos vc quer monstrar"))
while cont > 0:
    print(n1, " -> ", end="")
    aux = n1
    n1 = n2
    n2 += aux
    cont -= 1
print("FIM!")

    
    
