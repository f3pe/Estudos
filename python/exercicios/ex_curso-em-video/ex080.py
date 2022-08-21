#Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
def main():
    lista = list()
    for i in range(0, 5):
        n = int(input("Digite um valor: "))
        if i == 0 or n > lista[-1]:
            lista.append(n)
        else:
            for j, v in enumerate(lista):
                if n <= v: 
                    lista.insert(j, n)
                    break
    print(f"Os valores digitados em ordem crescente foram: {lista}")
if __name__=="__main__":
    main()