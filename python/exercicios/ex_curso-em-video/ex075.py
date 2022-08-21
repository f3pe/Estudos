#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
def main(): 
    valores = (int(input("Digite um numero: ")), int(input("Digite mais um numero: ")), int(input("Digite o terceiro numero: ")), int(input("Digite o ultimo numero: ")))
    print(valores)
    print(f"O numero 9 apareceu {valores.count(9)} vezes")
    if 3 in valores: print(f"O número três está na possição {valores.index(3)+1}")
    else: print("O número 3 não está denreo da tupla")
    print("Os numeros pares são: ", [i for i in valores if i % 2 == 0])
    
if __name__ == "__main__":
    main()