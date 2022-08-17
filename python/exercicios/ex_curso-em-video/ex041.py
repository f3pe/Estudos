from datetime import date
n = int(input("Digite o ano de nascimento do atleta: "))
idade = date.today().year - n
if 0 < idade <= 9:
    print("Esse é um atleta MIRIM")
elif 9 < idade <= 14:
    print("Esse é um atleta INFANTIL")
elif 14 < idade <= 19:
    print("Esse é um atleta JUNIOR")
elif 19 < idade <= 25:
    print("Esse é um atleta SÊNIOR")
elif 25 < idade:
    print("Esse é um atleta MASTER")
else:
    print("Esse atleta ainda não nasceu!")
