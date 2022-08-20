# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
#dei uma robadinha usando lista pra facilitar minha vida 
def main():
    print("-"*40)
    print("\tcaixa eletronico ")
    print("-"*40)
    valor = int(input("quanto vc gostaria de sacar: "))
    nota = [50, 20, 10, 1]
    for i in range(len(nota)): 
        qtdNotas, valor = divmod(valor , nota[i])
        if qtdNotas != 0:
            print(f"Total de notas de R${nota[i]:.2f}: {qtdNotas}")
    
if __name__ == '__main__':
    main()
