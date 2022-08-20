def main():
    numbers = ("um", "dois", "três", "Quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "cartoze", "quinze", "desesseis", "dezessete", "dezoito", "dezenove", "vinte")
    while True:
        num = int(input("Escolha um numero de 1 a 20: "))
        if 0 < num < 21: print(f"\nO numero selecionado foi {numbers[num-1]}"); break 
            
        else:print("\nOpção invalida, por favor selecione um numero na faixa solicitada\n")
if __name__ == '__main__':
    main()