from .node import Node

class Stack:
    def __init__(self):
        self.head = None
        self.capacity = 0

    def push(self, data):
        if (self.head == None):
            self.head = Node(data)
            capacity += 1
        else:
            newNode = Node(data)
            newNode.nextNode(self.head)
            self.head = newNode
            capacity += 1

    def pop(self):
        if (self.head == None):
            pass
        else:
            newHead = self.head.nextNode
            oldData = self.head.data
            del self.head
            self.head = newHead
            capacity -= 1
            return oldData
    def top(self):
        return self.head.data
    def capacity(self):
        return self.capacity

