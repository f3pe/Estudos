#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia(l, qtd):
    print(f"Sorteando {qtd} valores: ", end="")
    for i in range(qtd):
        i = randint(0, 99)
        print(f"{i} ", end="", flush=True)
        l.append(i)
        sleep(0.5)
    print("Pronto")

def sumPares(n):
    soma = 0
    for i in n:
        if i % 2 == 0:
            soma += i
    print(f"A soma dos números pares de {n} é: {soma}")


def main():
    numeros = list()
    sorteia(numeros, 5)
    sumPares(numeros)


if __name__=="__main__":
    main()