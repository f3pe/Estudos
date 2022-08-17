from datetime import date
ano = int(input("Digite o ano que gostaria de verificar(0 pra a data atual): "))
ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bixesto".format(ano))
else:
    print("O ano {} não é bixesto".format(ano))