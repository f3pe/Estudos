#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(num):
    maior = None;
    for i in num:
        if maior == None:
            maior = i
        elif maior < i:
            maior = i
    return maior
    
def mensagem(*num):
    print("=="*30)
    print("Analizando informações...")
    for i in num:
        print(f"{i} ", flush=True, end="")
        sleep(0.5)
    print(f"Foram informados {len(num)} valores.\nE o maior é {maior(num)}.")
    print("=="*30)

def main():
    mensagem(1,2,3,5,4,9)
    mensagem(4,8,6,5,8,4,92,8,4,58)
    mensagem(2,6,5,4,8,9,65,258,24,215,24,3)
    mensagem(636,369,3562,35,38,65,14)

if __name__=="__main__":
    main()