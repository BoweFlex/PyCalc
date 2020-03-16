from .node import Node

class Stack:
    def __init__(self):
        self.head = None
        self.capacity = 0

    def push(self, data):
        if (self.head == None):
            self.head = Node(data)
            self.capacity += 1
        else:
            newNode = Node(data)
            newNode.nextNode = self.head
            self.head = newNode
            self.capacity += 1

    def pop(self):
        if (self.head == None):
            pass
        else:
            newHead = self.head.nextNode
            oldData = self.head.data
            del self.head
            self.head = newHead
            self.capacity -= 1
            return oldData
    def top(self):
        return self.head.data
