class SimpleQueue:
    def __init__(self) -> None:
        self._queue = []
        self._length = -1
        self._cont = 0

    def __repr__(self) -> str:
        return f"{self.queue}"
    
    def __iter__(self):
        return self
    
    def __next__(self) -> any:
        if self._cont > self._length:
            self._cont = 0
            raise StopIteration
        current = self._queue[self._cont]
        self._cont += 1
        return current
    
    def enqueue(self, item) -> None:
        self._queue.append(item)
        self._length += 1

    def dequeue(self) -> any:
        self._length -= 1
        return self._queue.pop(0)

    def isEmpty(self) -> bool:
        return not (self._queue)
    
    def peek(self) -> any:
        return self._queue[0]
    
if __name__=="__main__":
    fila = SimpleQueue()
    fila.enqueue(1)
    fila.enqueue(2)
    fila.enqueue(3)
    print("For 1:")
    for i in fila:
        print(i)
    print("\n\nFor 2:")
    for i in fila:
        print(i)
    print("\n\nRemovendo 2 items:")
    print(f"item {fila.dequeue()} removido")
    print(f"item {fila.dequeue()} removido")
    print("\n\nA fila está vazia?")
    print(f"{fila.isEmpty()}")
    print(f"Proximo da fila: {fila.peek()}")
    
        
        