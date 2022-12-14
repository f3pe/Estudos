#Exercício Python 082: 
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

def main():
    lista = list()
    pares = list()
    impares = list()
    op = "S"
    while(op in "sS"):
        n = int(input("Digite um número: "))
        lista.append(n)
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
        op = input("deseja continuar? [s/n]: ")
    print(f"Lista completa: {lista} \n")
    print(f"Lista de números pares: {pares} \n")
    print(f"Lista de números ímpares: {impares} \n")

if __name__ == "__main__":
    main()



