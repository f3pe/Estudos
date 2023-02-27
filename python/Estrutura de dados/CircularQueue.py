class CircularQueue():
    def __init__(self, length) -> None:
        self.head = self.tail = -1
        self.length = length
        self.queue = [None] * length
        return
    
    def __repr__(self) -> str:
        return f"{self.queue}"

    def __iter__(self):
        self.nav = self.head
        self.cont = 0
        return self
    
    def __next__(self) -> any:
        if (self.nav == (self.tail + 1) % self.length ) and self.cont > 0:
            raise StopIteration
        self.cont += 1
        current = self.queue[self.nav]
        self.nav = (self.nav + 1) % self.length
        return current
        
    def enQueue(self, item) -> None:
        if self.isFull():
            print("Fila está cheia")
            return
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
            return
        else:
            self.tail = (self.tail + 1) % self.length
            self.queue[self.tail] = item
            return

    def deQueue(self) -> any:
        if self.isEmpty():
            print("A fila está vazia")
            return None
        elif self.head == self.tail:
            item = self.queue[self.head]
            self.head = self.tail = -1    
            return item
        else:
            item = self.queue[self.head]
            self.head = (self.head + 1) % self.length
            return item
        
    def peek(self) -> any:
        if self.isEmpty():
            print("Fila vazia")
            return
        else:
            return self.queue[self.head]
        
    def isFull(self) -> bool:
        return bool((self.tail + 1) % self.length == self.head)

    def isEmpty(self) -> bool:
        return bool(self.head == -1)


if __name__ == "__main__":
    fila = CircularQueue(3)
    for i in range(4):
        print(f"tentando adicionar {i} na fila ", end="")
        fila.enQueue(i)
        print()

    print("for 1: ")
    for i in fila:
        print(i)
    for i in range(3):
        print(f"Item {fila.deQueue()} removido ")
    print(f"A fila está vazia: {fila.isEmpty()}")


