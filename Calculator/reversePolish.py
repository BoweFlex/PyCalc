from .stack import Stack

class ReversePolish:
    def __init__(self):
        self.operators = ['^', '*', '/', '+', '-']

    @staticmethod
    def calculate(self, postfix="11+") -> int:
       for (token in postfix):
           if (token in self.operators):
               pass
