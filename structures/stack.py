class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return self.__str__()

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
    
    def peek(self):
        if self.head:
            return self.head.data
    
    def is_empty(self):
        return not self.head
    
    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False        

    def __str__(self) -> str:
        txt = ""
        node = self.head
        while node:
            txt += f"{node.data} -> "
            node = node.next
        return txt

    def __repr__(self) -> str:
        return self.__str__()