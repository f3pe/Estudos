#confere se um numero é primo ou não
cont = 1
n = int(input("Digite um numero: "))
for i in range(2, n):
    if n % i == 0:
        cont += 1
print("O numero {} foi dividido {} vezes".format(n, cont+1))
if cont > 1:
    print("O numero não é primo")
else:
    print("É um numero primo")
