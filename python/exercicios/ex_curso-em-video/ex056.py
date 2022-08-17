#analise de informaçoes de pessoas
soma = 0
maior = 0
maisVelho = ""
cont = 0
for i in range(1, 4):
    print("----- {}ª pessoa -----".format(i)) 
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo[m/f]: ")
    soma += idade
    if sexo == 'm' and idade > maior:
        maior = idade
        maisVelho = nome
    if sexo == 'f' and idade < 20:
        cont += 1
print("A media de idade do grupo é de {:.1f} anos".format(soma/3))
if maisVelho == "":
    print("Não teve nenhum homem na lista")
else:
    print("O homem mais velho tem {} anos e se chama {}".format(maior, maisVelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(cont))


