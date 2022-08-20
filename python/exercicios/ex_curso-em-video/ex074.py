from random import randint

def main():
    sorteado = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))
    print("Os valores sorteados foram ", end=" ")
    for i in sorteado: print(i, end=" ")
    print(f"\nOmaior valor sorteado foi {max(sorteado)}")
    print(f"O menor valor sorteado foi {min(sorteado)}")
if __name__ == "__main__":
    main()