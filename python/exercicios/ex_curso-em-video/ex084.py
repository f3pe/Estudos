#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves
def main():
    temp = list()
    princ = list()
    menor = maior = 0
    while True:
        temp.append(input("Nome: "))
        temp.append(float(input("Peso: ")))
        if len(princ) == 0:
            menor = maior = temp[1]
        if menor > temp[1]:
            menor = temp[1]
        if maior < temp[1]:
            maior = temp[1]
        princ.append(temp[:])
        temp.clear()
        op = input("continuar? [s/n]: ")
        if op in "nN":
            break
    print(f"Foram cadastradas {len(princ)} pessoas \nElas foram {princ}")
    print(f"O maior peso foi {maior:0.2f}KG de ", end="")
    for i in princ:
        if i[1] == maior:
            print(f" {i[0]} ", end="")
    print(f"\nO maior peso foi {menor:0.2f}KG de", end="")
    for i in princ:
        if i[1] == menor:
            print(f" {i[0]}", end="")


if __name__ == "__main__":
    main()