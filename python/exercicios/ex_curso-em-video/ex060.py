f = r = int(input("Digite um numero: "))
n = f-1
while n > 0:
    f = n * f
    n-=1
print("O fatorial de {} é {}".format(r, f))