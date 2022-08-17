soma = 0
n = 0
cont = 0
while n != 999:
    n = int(input("digite um numero [999 para parar]: "))
    if n != 999:
        soma += n
        cont += 1
print("Foram digitados {} numeros e a somas deles é {}".format(cont, soma)) 