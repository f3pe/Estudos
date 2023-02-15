def ajuda(com):
    help(com)

def main():
    while True:
        comando = str(input("Digite a função ou biblioteca > "))
        if comando.upper() == "FIM":
            return
        ajuda(comando)

if __name__=="__main__":
    main()