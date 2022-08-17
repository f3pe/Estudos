n = int(input("Digite um numero: "))
print("Analisando o numero: {}".format(n))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print("""
Unidade {}
Dezena {}
Centena {}
Milhar {} """.format(u,d,c,m))