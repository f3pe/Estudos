def area(c, l):
    print(f"O terreno {c}x{l} tem {c*l}m² de área")

def main():
    print("Controle de terreno")
    print("_"*20)
    a = float(input("Digite a comprimento do terreno(em metros): "))
    b = float(input("Digite a largura do terreno(em metros): "))
    area(a, b)
    

if __name__=="__main__":
    main()