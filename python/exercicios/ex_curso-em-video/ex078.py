#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
def main():
    n = list()
    menor = maior = 0
    for c in range(0, 5):
        n.append(int(input("Digite um numero: ")))
        if c == 0: menor = maior = n[c]
        if n[c] < menor: menor = n[c]
        if n[c] > maior: maior = n[c]
    print(f"O maior numero foi {maior} é apareceu nas posições ", end="")
    for i,v in enumerate(n):
        if v == maior:
            print(f"{i+1}...", end="")
    print(f"\nO menor numero foi {menor} é apareceu nas posições ", end="")
    for i,v in enumerate(n):
        if v == menor:
            print(f"{i+1}...", end="")
if __name__ == '__main__':
    main()