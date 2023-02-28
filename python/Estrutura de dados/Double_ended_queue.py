class deque:
    def __init__(self) -> None:
        self._queue = []
        return
    def __repr__(self) -> str:
        return f"{self._queue}"
    
    def __iter__(self):
        self.nav = 0
        return self
    
    def __next__(self) -> any:
        if self.nav == self.size():
            raise StopIteration
        else:
            _current = self.nav
            self.nav += 1
            return self._queue[_current]

    def isEmpty(self) -> bool:
        return not bool(self._queue)
    
    def addRear(self, item) -> None:
        self._queue.append(item)
        return
    
    def addFront(self, item) -> None:
        self._queue.insert(0, item)
        return
    
    def removeFront(self) -> any:
        return  self._queue.pop(0)
    
    def removeRear(self) -> any:
        return self._queue.pop()
    
    def size(self) -> int:
        return len(self._queue)
    
if __name__ == "__main__":
    fila = deque()
    fila.addFront(1)
    fila.addFront(2)
    fila.addFront(3)
    fila.addRear(9)
    print(f"A fila está vazia: {fila.isEmpty()}")
    print(fila)
    print("For 1:")
    for i in fila:
        print(i, end=" - ")
    print("\nFor 2:")
    for i in fila:
        print(i, end=" - ")
    fila.removeFront()
    fila.removeRear()
    print("\nFor 3:")
    for i in fila:
        print(i, end=" - ")
    print(f" Tamanho da fila {fila.size()}")
    
    
