#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
import datetime
def voto(n):
    data = datetime.date.today().year
    idade = data - n
    print(f"Com {idade} anos o voto: ", end="")
    if (idade > 70 or 15 < idade < 18):
        print("FACULTATIVO")
    elif (idade < 16):
        print("NÃO VOTA")
    else:
        print("OBRIGATORIO")
def main():
    print("-"*20)
    voto(int(input("Digite seu ano de nascimento: ")))

if __name__ == "__main__":
    main()