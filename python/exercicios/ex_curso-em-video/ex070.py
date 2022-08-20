def main():
    print("-"*40)
    print("\t\tLoja")
    print("-"*40)
    op = 'S'
    menP = soma = contM = 0
    prodB = ''
    while op == 'S':
        prod = input("Digite o nome do produto: ")
        preco = float(input(f"Digite o preço de {prod}: "))
        if preco < menP or menP == 0: 
            menP = preco
            prodB = prod
        if preco > 1000: contM += 1
        soma += preco
        while True:
            op = input("Gostaria de continuar?[S/N]: ").upper()
            if op in "NS": break
            print("opção invalida: \n\n")
    print(f"\n\nO total da compra foi R${soma:.2f} ")
    print(f"{contM} produtos custam mais de R%1000,00")
    print(f"O produto mais barato foi {prodB} custando R${menP:.2f} ")    

if __name__ == "__main__":
    main()