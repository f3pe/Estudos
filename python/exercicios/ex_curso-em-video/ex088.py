from time import sleep
from random import randint
jogo = list()
cont = 1
print("="*30)
print(f"{'JOGA NA MEGA SENA':>23}")
print("="*30)
times = int(input("Quantos jogos devo sortear? "))
while times >= cont:
    i = 0
    if times < 0:
        break
    while i < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
            i += 1
    jogo.sort()
    print(f"jogo {cont}:{jogo}")
    jogo.clear()
    cont += 1
    sleep(1)
print("==========Boa sorte==========")