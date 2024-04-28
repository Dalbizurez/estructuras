class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return self.__str__()
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new = Node(data)
        if self.head:
            node = self.head
            while node.next:
                node = node.next
            node.next = new
        else:
            self.head = new
    
    def prepend(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def delete(self, data):
        if self.head:
            if self.head.data == data:
                self.head = self.head.next
                return
            node = self.head
            prev = None
            while node.next:
                if node.data == data:
                    prev.next = node.next
                    return
                prev = node
                node = node.next

    def __str__(self) -> str:
        txt = ""
        node = self.head
        while node:
            txt += f"{node.data} -> "
            node = node.next
        return txt

    def __repr__(self) -> str:
        return self.__str__()