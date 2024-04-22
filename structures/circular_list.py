class Node:
    def __init__(self, data) -> None:
        self.next:Node = None
        self.data = data

    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return self.__str__()
    
class CircularList:
    def __init__(self) -> None:
        self.head:Node = None
        self.current:Node = None
    
    def append(self, data) -> None:
        new = Node(data)
        if self.head:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = new
            new.next = self.head
        else:
            self.head = new
            self.current = self.head
            new.next = self.head
        
    def prepend(self, data) -> None:
        new = Node(data)
        if self.head:
            node = self.head
            while node.next != self.head:
                node = node.next
            node.next = new
            new.next = self.head
            self.head = new
        else:
            self.head = new
            self.current = self.head
            new.next = self.head
            
    def lrotate(self) -> None:
        node = self.current
        while node.next != self.current:
            node = node.next
        self.current = node

    
    def rrotate(self) -> None:
        self.current = self.current.next
    
    def search(self, data) -> Node:
        node = self.head
        while node.data != data:
            node = node.next
            if node == self.head:
                return None
        self.current = node
        return node
    
    def delete(self, head:bool) -> None:
        if self.head.next == self.head:
            self.head = None
            self.current = None
            return
        node = self.head
        prev = node
        if head:
            while node.next != self.head:
                node = node.next
            node.next = self.head.next
            self.head = self.head.next
        else:
            while node.next != self.head:
                prev = node
                node = node.next
            if self.current == node:
                self.current = prev
            prev.next = self.head
    
    def __str__(self) -> str:
        if not self.head:
            return "#"
        node = self.head
        txt = f"{node} -> "
        while node.next != self.head:
            node = node.next
            txt += f"{node} -> "
        return txt
    
    def __repr__(self) -> str:
        return self.__str__()


            
    