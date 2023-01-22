#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    """
        -> Calcula o fatorial de um número 
        param: n <- O número a ser calculado
        param: show <- monstra o calculo ou não(opcional)
        return: printa na tela o fatorial de n
    """
    result = 1
    for i in range(n, 1, -1):
        result *= i
        if (show):
            print(F"{i} x ", end="")

    if (show):
        print(F"1 = {result}")
        return
    print(F"{result}")

def main():
    fatorial(5, show=False)


if __name__ == "__main__":
    main()