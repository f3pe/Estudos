#Esse código tem por objetivo simular as operações feitas em uma pilha(stack)
#No futuro irei fazer um código criando um objeto para ser uma pilha(stack) de fato, o objetivo desse código é ser algo conceitual
def isEmpty(lista):
    return not bool(len(lista))

def main():
    stack = []
    while True:
        print("-"*40)
        print(f"Pilha(stack)".center(40))
        print("-"*40)
        print(
            """
[1] - Adicionar um elemento
[2] - Remover um elemento(ultimo)
[3] - Verificar se está vazia
[4] - Ver o valor do ultimo elemento
[5] - Ver o tamanho da pilha
[6] - Ver toda a pilha
[7] - Sair
            """)
        while True:
            try:
                res = int(input("Resposta: "))
                break
            except ValueError:
                print("Erro! Por favor digite um numero valido")
        if(res == 1):
            stack.append(input("Digite o elemento que deseja adicionar: "))
        elif(res == 2):
            if not isEmpty(stack):
                i = stack.pop() 
                print(f"Item {i} removido")
                input("Aperte enter para continuar...")
            else:
                print("A pilha já está vazia!")
                input("Aperte enter para continuar...")
        elif(res == 3):
            print(f"A pilha está vazia: {isEmpty(stack)}")
            input("aperte enter para continuar..")
        elif(res == 4):
            print(f"O valor do ultimo elemento é: {stack[-1]}")
            input("Aperte enter para continuar...")
        elif(res == 5):
            print(f"O tamanho da pilha é {len(stack)}")
            input("Aperte enter para continuar...")
        elif (res == 6):
            for i in stack[::-1]:
                print(f"| {i:^5} |")
            input("Aperte enter para continuar...")
        elif (res == 7):
            break
        else:
            print("Por favor informe um valor valido")
            input("Aperte enter para continuar...")


if __name__=="__main__":
    main()
