#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

def main():
    vogais = ('a', 'e', 'i', 'o', 'u')
    palavras = ('Grito', 'Flautas' , 'Pare', 'Palito', 'Cisne')
    for i in palavras:
        print(f"\nNa palavra {i.upper()} temos", end=" ")
        for j in i: 
            if j.lower() in vogais: print(j, end=" ")
if __name__=="__main__":
    main()