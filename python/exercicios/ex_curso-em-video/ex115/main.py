import gerenciadorArquivo as ga

def main():
    while(True): 
        print("-"*40)
        print("Menu".center(40))
        print("-"*40)
        print("[1] - Adicionar um nome no arquivo")
        print("[2] - Listar pessoas cadastradas")
        print("[0] - Sair")
        resposta = input("Resposta => ")
        if(resposta == '1'):
            ga.add()
        elif(resposta == '2'):
            ga.listar()
        elif(resposta == '0'):
            break
        else:
            print("Digite uma opção valida")
if __name__=="__main__":
    main()
