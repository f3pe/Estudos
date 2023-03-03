class node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class linkedList:
    def __init__(self) -> None:
        self._current = None
        self.head = None

    def __repr__(self) -> str:
        s = ""
        for i in self:
            s += i + " "
        return s
    
    def __iter__(self):
        self._current = self.head
        return self
    
    def __next__(self) -> any:
        if self._current == None:
            raise StopIteration
        temp = self._current
        self._current = self._current.next
        return temp.item
