# confere se uma frase é um palidromo
frase = input("Digite sua frase: ").strip().upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
"""for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]"""
if inverso == junto:
    print("É palídromo!")
else:
    print("Não é palídromo!")
