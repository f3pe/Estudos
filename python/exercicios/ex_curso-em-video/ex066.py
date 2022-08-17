#Programa para o usuario digitar quantos números quiser, e depois o programa monstra a soma e a quantidade de numeros digitados
soma = cont = 0
while True:
    n = int(input("Digite um numero(999 para parar): "))
    if n == 999: break
    soma += n
    cont += 1
print(f"Foram {cont} números digitados e a soma deles é {soma}.")