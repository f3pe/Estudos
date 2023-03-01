class node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

class linkedList:
    def __init__(self, item=None) -> None:
        if item:
            self.head = node(item)
        else:
            self.head = None
        return
    
    def show(self) -> str:
        struct = ""
        nav = self.head
        while(nav):
            struct += f"{nav.item} "
            nav = nav.next
        return struct

if __name__=="__main__":
    lista = linkedList(2)
    print(lista.show())

#Essa lista vai servir como base para os códigos de stack e queue que farei no futuro
