from .stack import Stack

operators = ['^', '*', '/', '+', '-']

class ReversePolish:

    """ Utilizes a stack to calculate the result of a postfix notation expression """
    @staticmethod
    def exprCalc(postfix):
        print(postfix)
        operandStack = Stack()
        
        for token in postfix:
            print(token)
            try:
                operandStack.push(float(token))
                print(operandStack.top())
            except ValueError:
                if (token == ' '):
                    None
                elif (token in operators):
                    operand1 = operandStack.pop()
                    operand2 = operandStack.pop()
                    if (token == "+"):
                        result = operand1 + operand2
                    elif (token == "-"):
                        result = operand1 - operand2
                    elif (token == "*"):
                        result = operand1 * operand2
                    elif (token == "/"):
                        result = operand1 / operand2
                    else:
                        result = operand1**operand2
                    operandStack.push(result)
                else:
                    print("Not a number or operator")
        return operandStack.pop()

    """ Utilizes the shunting yard algorithm to change infix notation to postfix """
    @staticmethod
    def shuntParse(infix):
        output = ""
        operatorStack = Stack()
        
        for token in infix:
            print(output)
            try:
                float(token)
                output = output + ' ' + token
            except ValueError:
                if (token == ' '):
                    None
                elif ((token in operators) and (operatorStack.capacity > 0)):
                    while((operators.index(operatorStack.top()) > operators.index(token)) or (operators.index(operatorStack.top()) == operators.index(token))):
                        output = output + ' ' + operatorStack.pop()
                    operatorStack.push(token)
                elif ((token == '(') or (token in operators)):
                    operatorStack.push(token)
                elif (token == ')'):
                    while (operatorStack.top() != '('):
                        # If stack runs out without finding a left paren, parentheses are not matched
                        output = output + ' ' + operatorStack.pop()
                    operatorStack.pop()

        while (operatorStack.capacity != 0):
            output = output + ' ' + operatorStack.pop()
        
        return output
