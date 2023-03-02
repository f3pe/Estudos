from linked_list import linkedList
from linked_list import node

class stack:
    def __init__(self) -> None:
        self._stack = linkedList()
        self._length = 0

    def __repr__(self) -> str:
        s = ""
        _current = self._stack.head
        while(_current.next):
            s += f"{_current.item} "
            _current = _current.next
        s += f"{_current.item} "
        return s
    
    def __len__(self) -> int:
        return self._length
    
    def __iter__(self):
        if not self.isEmpty():
            self._current = self._stack.head
        else:
            self._current = None
        return self
    
    def __next__(self):
        if self._current == None:
            raise StopIteration 
        temp = self._current
        self._current = self._current.next
        return temp.item
    
    def push(self, item) -> None:
        self._length += 1
        if self._stack.head == None:
            self._stack.head = node(item)
        else:
            _current = self._stack.head
            while(_current.next):
                _current = _current.next
            _current.next = node(item)

    def pop(self) -> any:
        
        if self._length == 1:
            temp = self._delete(self._stack.head)
            self._length -= 1
            return temp
        elif self._length > 1:
            index = 1
            _current = self._stack.head
            while(index < self._length):
                _current = _current.next
                index += 1
            temp = self._delete(_current)
            self._length -= 1
            return temp
        
    def _delete(self, node) -> any:
        temp = node.item
        node = None
        return temp
        
    def peek(self) -> any:
        if not self.isEmpty():
            _current = self._stack.head
            while(_current.next):
                _current = _current.next
            return _current.item
    
    def isEmpty(self) -> bool:
        return not bool(self._length)

if __name__=="__main__":
    f = stack()
    print("-"*40)
    print("Teste da stack".center(40))
    print("-"*40)
    palavra = input("Digite uma palavra: ")
    for i in palavra:
        f.push(i)
    print(f"ultima letra da palavra: {f.peek()}")
    inverse = ""
    times = len(f)
    for i in range(times):
        inverse += f.pop()
    print(f"A palavra ao contrario fica: {inverse}")