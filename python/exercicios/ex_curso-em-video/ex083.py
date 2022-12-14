# Exercício Python 083: 
# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
def main():
    thing = str(input("Digite sua expressão: "))
    open = close = 0
    for i in thing:
        if i == '(':
            open += 1
        if i == ')':
            close += 1
    if open - close == 0:
        print("Sua espressão está correta!")
    else:
        print("Sua expressão está errada")

if __name__ == "__main__":
    main()