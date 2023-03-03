from linked_list import linkedList
from linked_list import node
import os

class stack:
    def __init__(self) -> None:
        self._stack, self._length = linkedList(), 0

    def __repr__(self) -> str:
        return self._stack
    
    def __len__(self) -> int:
        return self._length
    
    def __iter__(self):
        self._stack = self._stack.__iter__()
        return self
    
    def __next__(self):
        return self._stack.__next__() 
    
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
        if self._length >= 1:
            index, _current = 1, self._stack.head
            while(index < self._length):
                _current = _current.next
                index += 1
            self._length -= 1
            return self._delete(_current)
        else:
            raise Exception("Stack is Empty")
        
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
    os.system('cls')
    print("A palavra é: ", end="")
    for i in f:
        print(i, end="")
    print(f"\nUltima letra da palavra: {f.peek()}")
    inverse = ""
    times = len(f)
    for i in range(times):
        inverse += f.pop()
    print(f"A palavra ao contrario fica: {inverse}")
