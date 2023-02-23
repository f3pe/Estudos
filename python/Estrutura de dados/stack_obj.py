#Deu preguiça de fazer o __inter__ pra exibir cada elemento de forma mais bonita do que só usar o print na lista 🙃
class stack:
    def __init__(self) -> None:
        self.__MAX_ITEMS = 100
        self.stack = []
    
    def push(self, item) -> None:
        if len(self.stack) == self.__MAX_ITEMS:
            raise Exception("pilha cheia")
        self.stack.append(item)

    def pop(self) -> any:
        if(stack.isEmpty(self)):
            raise Exception("pilha está Vazia")
        return self.stack.pop()

    def isEmpty(self) -> bool:
        return not bool(self.stack)
    
    def isFull(self) -> bool:
        return len(self.stack) == self.__MAX_ITEMS
            
    def peek(self) -> any:
        if(stack.isEmpty(self)):
            raise Exception("pilha vazia")
        return self.stack[-1]
    
    def __repr__(self) -> str:
        return str(self.stack)
    
    def len(self) -> int:
        return len(self.stack)
    
def main():
    pilha = stack()
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
            if(pilha.isFull()):
                print("pilha já está cheia")
                input("enter para continuar..")
                continue
            pilha.push(input("Digite o elemento que deseja adicionar: "))

        elif(res == 2):
            if not pilha.isEmpty(): 
                print(f"Item {pilha.pop()} removido")
                input("Aperte enter para continuar...")
            else:
                print("A pilha já está vazia!")
                input("Aperte enter para continuar...")
        elif(res == 3):
            print(f"A pilha está vazia: {pilha.isEmpty()}")
            input("aperte enter para continuar..")
        elif(res == 4):
            print(f"O valor do ultimo elemento é: {pilha.peek()}")
            input("Aperte enter para continuar...")
        elif(res == 5):
            print(f"O tamanho da pilha é {pilha.len()}")
            input("Aperte enter para continuar...")
        elif (res == 6):
            print(f"pilha: {pilha}")
            input("Aperte enter para continuar...")
        elif (res == 7):
            break
        else:
            print("Por favor informe um valor valido")
            input("Aperte enter para continuar...")

if __name__=="__main__":
    main()