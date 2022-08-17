largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura*altura
tinta = area/2
print("A sua parede tem dimenção de {}x{} e tem uma area de {}m²".format(largura, altura, area))
print("E para pintar essa parede voce vai precisar de {}L  de tinta".format(tinta))
