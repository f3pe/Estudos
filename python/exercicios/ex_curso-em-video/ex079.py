#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente
def main():
    lista = list()
    op = 's'
    while op in 'sS':
        n = int(input("Digite um valor: "))
        if n not in lista: lista.append(n)
        else: print(f"\nO valor {n} já foi adicionado\n")
        while True:
            op = input("Deseja continuar?[S/N]: ")[0]
            if op in "sSnN": break
            else: print("\nOpção invalida\n")
    print(f"Os numeros digitados foram: {sorted(lista)}")
            
if __name__ == '__main__':
    main()