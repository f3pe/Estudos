#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
def main():
    prod = ("processador", 500.00, "placa mãe", 600.00, "placa de vídeo ", 1000.00, "fonte", 300.00, "gabinete", 150.00)
    print("="*40)
    print(f"{'Lista de compras':>28}")
    print("="*40)
    for i in range(0, len(prod), 2):
        print(f"{prod[i]:.<30}", end="")
        print(f" {prod[i+1]:>7.2f}")
if __name__== "__main__":
    main()