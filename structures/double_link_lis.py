class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return self.__str__()
    
class DoubleLinkedList:
    def __init__(self):
        self.head:Node = None
        self.tail:Node = None
    
    def append(self, data):
        new =  Node(data)
        if self.head:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        else:
            self._insert_head(new)
    
    def _insert_head(self, new):
        self.head = new
        self.tail = new
        

    def prepend(self, data):
        new = Node(data)
        if self.head:
            self.head.prev = new
            new.next = self.head
            self.head = new
        else:
            self._insert_head(new)

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False 

    def delete(self, head):
        if not self.head.next:
            self.head = None
            self.tail = None
            return
        if head:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def __str__(self) -> str:
        txt = ""
        node = self.head
        while node:
            txt += f"{node.data} <-> "
            node = node.next
        return txt
    
    def __repr__(self) -> str:  
        return self.__str__()