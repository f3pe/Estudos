def leiaInt(frase):
    """
        frase:Frase que sera exibida no terminal para perdir o número    
    """
    ok = False
    while(not ok):
        n = input(frase)
        ok = True
        for i in n:
            if (ord(i) > 58) or (ord(i) < 48):# compara a letra com o ascii dos numero de 0 a 9
                ok = False
                print("ERRO! Digite um número valido")
                break
    return n
            
def main():
    n = leiaInt("Digite um número inteiro: ")
    print(f"O número digitado foi {n}.")

if __name__=="__main__":
    main()