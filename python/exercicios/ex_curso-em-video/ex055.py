#verificar o maior peso e o menor
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input("Digite o peso da {}º pessoa".format(i)))
    if i == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print("O maior peso lido foi de {:.1f}Kg\n e o menor peso lido foi de {:.1f}Kg".format(maior, menor))