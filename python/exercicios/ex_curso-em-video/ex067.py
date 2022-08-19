#O programa deve exibir a tabuada de qualquer número até o 10 e depois perguntar se deseja ver a tabuada de outro numero
#Caso sejá digitado um número negativo o programa deve finalizar
#Nesse exercicio estou praticando um conceito que não foi ensinado no curso em video, usando o if __name__ == '__main__', quero dizer que esse é um script executável 
def main():
    while True:
        number = int(input("Digite o numero que você quer ver a tabuada: "))
        if number < 0: break
        print("-"*30)
        for i in range(1, 11): print(f" {number} x {n:2} = {number*i:3}")
        print("-"*30)


if __name__ == '__main__':
    main()