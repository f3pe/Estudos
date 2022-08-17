from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = dict()
print("Valores sorteados")
for i, j in jogo.items():
    print(f"O jogador {i} tirou {j} no dado")
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("== Os vencedores ==")
for i in range(0, 4):
    print(f" {i+1}º {ranking[i][0]} : {ranking[i][1]} ")