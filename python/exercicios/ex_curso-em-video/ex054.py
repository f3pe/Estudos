#confere se é maior de idade
from datetime import date
maior = 0
menor = 0
for i in range(1, 8):
    nascimento = int(input("Em qual ano a {}ºpessoa nasceu: ".format(i)))
    if nascimento - date.today().year >= 18:
        maior += 1
    else:
        menor += 1
print("Tiveram {} pessoas de maior".format(maior))
print("E tiveram {} pessoas de menor".format(menor))
