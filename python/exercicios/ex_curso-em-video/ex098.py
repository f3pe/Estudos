#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
from time import sleep

def contar (inicio, fim, passo):
    if passo < 0: 
        passo *= -1
    if passo == 0:
        passo = 1 
    print("-="*30)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if inicio < fim:
        for i in range(inicio, fim, passo):
            print(f" {i}  ", end="", flush=True)
            sleep(0.5)
        print("FIM!")
    if inicio > fim:
        for i in range(inicio, fim, -passo):
            print(f" {i}  ", end="", flush=True)
            sleep(0.5)
        print("FIM!")

def main():
    contar(1, 10, 1)
    contar(10, 0, 2)
    print("-="*30)
    inicio = int(input("inicio: "))
    fim = int(input("fim: "))
    passo = int(input("passo: "))
    contar(inicio, fim, passo)

if __name__=="__main__":
    main()