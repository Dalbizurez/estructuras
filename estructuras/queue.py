class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return str(self.data)
    
    def __repr__(self) -> str:
        return self.__str__()

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new = Node(data)
        if self.head:
            new.next = self.head
            self.head =  new
        else:
            self.head = new
            self.tail = new
    
    def dequeue(self):
        if self.head:
            data = self.tail.data
            node = self.head
            if node == self.tail:
                self.head = None
                self.tail = None
                return data
            while node.next != self.tail:
                node = node.next
            node.next = None
            self.tail = node
            return data

    def peek(self):
        if self.tail:
            return self.tail.data

    def is_empty(self):
        return not self.head

    def __str__(self) -> str:
        txt = ""
        node = self.head
        while node:
            txt += f"{node.data} -> "
            node = node.next
        return txt