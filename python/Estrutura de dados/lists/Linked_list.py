class node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class linkedList:
    def __init__(self) -> None:
        self._current = None
        self.head = None
    
