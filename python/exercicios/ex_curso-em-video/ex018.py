import math
angulo = float(input("Digite o angulo que vc que ver: "))
angulo = math.radians(angulo)
print("O seno desse angulo é: {:.2f}".format(math.sin(angulo)))
print("O coseno desse angulo é: {:.2f}".format(math.cos(angulo)))
print("O tangente desse angulo é: {:.2f}".format(math.tan(angulo)))