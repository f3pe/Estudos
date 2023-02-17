#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(frase):
    """
        frase:Frase que sera exibida no terminal para perdir o número    
    """
    validNum = False
    while(not validNum):
        try:
            validNum = True
            num = int(input(frase))
        except KeyboardInterrupt or UnboundLocalError:
            num = 0
            print("O usuario não digitou nada")
        except:
            validNum = False
            print("ERRO! Digite um número inteiro valido")
    return num

def leiaFloat(frase):
    """
        frase:Frase que sera exibida no terminal para perdir o número    
    """
    validFloat = False
    while(not validFloat):
        try:
            validFloat = True
            dotNum = float(input(frase))
        except KeyboardInterrupt or UnboundLocalError:
            dotNum = 0
            print("O usuario não digitou nada")
        except:
            validFloat = False
            print("Erro! Digite um numero real valido")
    return dotNum

            
def main():
    number = leiaInt("Digite um número inteiro: ")
    dotNumber = leiaFloat("Digite um número real: ")
    print(f"O número inteiro digitado foi:\t{number}")
    print(f"O número real digitado foi:\t{dotNumber}")

if __name__=="__main__":
    main()