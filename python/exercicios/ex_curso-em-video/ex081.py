#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.


def main():
    lista = list()
    op = "S"
    n = 5
    while(op in "sS"):
        lista.append(int(input("Digite um número: ")))
        op = input("deseja continuar? [s/n]: ")
    print(sorted(lista, reverse=True), "\n")
    print(f"foram digitados {len(lista)} números \n")
    if 5 in lista:
        print(f"O valor {n} está na lista \n" )

if __name__ == "__main__":
    main()