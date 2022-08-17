from datetime import date
ano = int(input("ano de nascimento: "))
alistamento_certo = ano + 18
if alistamento_certo < date().year:
    print("seu alistamento já passou, ele deveria ter ocorrido em {}".format(alistamento_certo))
elif alistamento_certo > date().year:
    print("seu alistamento ainda não ocorreu, ele será no ano de {}".format(alistamento_certo))
else:
    print("Seu alistamento será nesse ano, compareça ao quartel ou realize o alistamento online")