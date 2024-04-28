class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return self.__str__()
    
class DoubleLinkedCircularList:
    def __init__(self):
        self.head:Node = None
        self.tail:Node = None
        self.current:Node = None
    
    def append(self, data):
        new =  Node(data)
        if self.head:
            self.tail.next = new
            new.prev = self.tail
            self.head.prev = new
            new.next = self.head
            self.tail = new
        else:
            self._insert_head(new)
    
    def _insert_head(self, new):
        self.head = new
        self.tail = new
        new.next = self.head
        new.prev = self.tail
        self.current = self.head
        

    def prepend(self, data):
        new = Node(data)
        if self.head:
            self.head.prev = new
            self.tail.next = new
            new.next = self.head
            new.prev = self.tail
            self.head = new
        else:
            self._insert_head(new)
        
    def delete(self, head):
        if self.head.next == self.head:
            self.head = None
            self.tail = None
            return
        if head:
            temp = self.head
            self.head = temp.next
            self.tail.next = self.head
            self.head.prev = self.tail
            del temp
        else:
            temp = self.tail
            self.tail = temp.prev
            self.head.prev = self.tail
            self.tail.next = self.head
            del temp
    
    def lrotate(self):
        self.current = self.current.prev
    
    def rrotate(self):
        self.current = self.current.next

    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                self.current = node
                return True
            node = node.next
            if node == self.head:
                break
        return False

    def __str__(self) -> str:
        txt = ""
        node = self.head
        while node:
            txt += f"{node.data} <-> "
            node = node.next
            if node == self.head:
                break
        return txt
    
    def __repr__(self) -> str:
        return self.__str__()