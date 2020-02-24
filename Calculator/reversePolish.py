from .stack import Stack

operators = ['^', '*', '/', '+', '-']

class ReversePolish:

    """ Utilizes a stack to calculate the result of a postfix notation expression """
    @staticmethod
    def exprCalc(postfix):
        operandStack = Stack()
        
        for token in postfix:
            print(token)
            if (token in operators):
                operand1 = operandStack.pop()
                operand2 = operandStack.pop()
                result = operand1 + operand2
                operandStack.push(result)
            
            elif ((isinstance(token, int)) or (isinstance(token, float))):
                # Maybe change this to be a try - catch if it just displays token as string 
                # where it tries to convert token to int or float
                operandStack.push(token)
            else:
                pass
        return operandStack.pop()

    """ Utilizes the shunting yard algorithm to change infix notation to postfix """
    @staticmethod
    def shuntParse(infix):
        output = ""
        operatorStack = Stack()
        
        for token in infix:
            if ((isinstance(token, int)) or (isinstance(token, float))):
                output += token

            elif (token in operators):
                while ((operators.index(operatorStack.top()) > operators.index(token)) or 
                        ((operators.index(operatorStack.top()) == operators.index(token)) and 
                            token != '^')):
                    output += operatorStack.pop()
                operatorStack.push(token)

            elif (token == '('):
                operatorStack.push(token)

            elif (token == ')'):
                while (operatorStack.top() != '('):
                    # If stack runs out without finding a left paren, parentheses are mismatched
                    output += operatorStack.pop() 
                operatorStack.pop()

        while (operatorStack.capacity() != 0):
            output += operatorStack.pop()
        
        return output

