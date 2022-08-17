from random import randint
from time import sleep
print("-=-"*20)
print("Vou pensar em um numero entre 0 e 5, tente adivinhar")
print("-=-"*20)
n = int(input("Seu chute: "))
mistery_number = randint(0, 5)
print("processando...")
sleep(1)
if(n == mistery_number):
    print("Parabens você acertou!")
else:
    print("Você errou, o numero era {}, tente novamente".format(mistery_number))
