def add():
    print("-"*40)
    print("Adicionar pessoa".center(40))
    print("-"*40)
    with open("pessoas.txt", "a+") as file:
        try:
            nome = str(input("Digite o nome da pessoa: "))
        except:
            print("Nenhum valor digitado, voltando ao menu principal")
            return
        while(True):
            try:
                idade = int(input("Digite a idade dessa pessoa: "))
            except KeyboardInterrupt or UnboundLocalError:
                print("ERRO! Nenhuma idade digitada")
                file.write(f"{nome:<30} NULL\n.")
                return
            except:
                print("ERRO! Por favor digite um número inteiro para a idade")
            else:
                file.write(f"{nome:<30} {idade}\n")
                break

def listar():
    print("-"*40)
    print("Lista de pessoas".center(40))
    print("-"*40)
    with open("pessoas.txt", "r") as file:
        linhas = file.readlines()
        for i in range(0, len(linhas)):
            print(linhas[i], end="")
        print()
