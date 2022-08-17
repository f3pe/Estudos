from random import randint
from time import sleep
op = int(input("""
Escolha sua opção
[1] tesoura
[2] pedra
[3] papel
Resposta do jogador: """))
pc = randint(1, 3)
print(pc)
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
if op == pc:
    print("=+="*20)
    print(" O resultado foi: Empate")
    print("=+="*20)
elif op == 1 and pc == 2 or op == 2 and pc == 3 or op == 3 and pc == 1:
    print("=+="*20)
    print(" O resultado foi: Computar venceu")
    print(" Mais sorte na proxima")
    print("=+="*20)
elif op == 1 and pc == 3 or op == 2 and pc == 1 or op == 3 and pc == 2:
    print("=+="*20)
    print(" O resultado foi: Jogador venceu")
    print(" Parabens")
    print("=+="*20)
else:
    print("opção invalida")