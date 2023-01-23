#Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome = "desconhecido", gols = '0'):
    print(f"O Jogador {nome} fez {gols} gols")


def main():
    a = input("Digite o nome do jogador: ")
    b = input("Quantos gols ele fez: ")
    if(a == "" and b == ""):
        ficha()
    elif (a == ""):
        ficha(gols=b)
    elif (b == ""):
        ficha(nome=a)
    else:
        ficha(a, b)

if __name__=="__main__":
    main()