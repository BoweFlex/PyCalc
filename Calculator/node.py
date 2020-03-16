
""" Utilized by stack.py to create a linked list for a dynamic, efficient stack """
class Node:
    def __init__(self, data = int):
        self.data = data
        self.nextNode = None
