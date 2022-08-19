#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

def main():
    cont = 0
    while True: 
        print('=-'*20)
        print("Vamos jogar par ou impar")
        print('=-'*20)
        value = int(input("digite um valor: "))
        while True:
            par_impar = input("Quer par ou impar[P/I]: ").upper()
            if par_impar in 'PI':break
            else: print("Opção invalida \n")
        computador = randint(1, 10)
        print('-'*40)
        vencedor = 'par' 
        if (value + computador) % 2 == 1: vencedor = 'impar'
        print(f"Você jogou {value} o computador jogou {computador} o resultado foi {vencedor}")
        print('-'*40)
        if vencedor == 'par' and par_impar == 'P' or vencedor == 'impar' and par_impar == 'I': 
            print("Você venceu")
            cont += 1
        else: 
            print("O computador venceu")
            break
    print('=-'*20)
    print(f"Você venceu por {cont} vezes consecutivas")

if __name__ == '__main__':
    main()