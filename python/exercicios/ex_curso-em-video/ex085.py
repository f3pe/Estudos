#Exercício Python 085: 
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

def main():
    lista = [[], []]
    for i in range(1, 8):
        n = int(input(f"Digite O {i}º número: "))
        if n % 2 == 1:
            lista[1].append(n)
        else:
            lista[0].append(n)
    lista[0].sort()
    lista[1].sort()
    print(f"Os número pares foram: {lista[0]}")
    print(f"Os número ímpares foram: {lista[1]}")

if __name__ == "__main__":
    main()