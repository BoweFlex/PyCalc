import sys
from Calculator import ConsoleInput
from Calculator import ReversePolish

def main():
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to Jonathan's Calculator program!")
    print("+++++++++++++++++++++++++++++++++++++++++\n")
    
    print("++++Choose quit at any time to exit.+++++\n")
    
    mainInput()
    
    while (ConsoleInput.get_further_input() != "no"):
        mainInput()

    sys.exit()

if __name__ == "__main__":
    main()

def mainInput():
    #Uses ConsoleInput and ReversePolish to receive input and calculate answer
    calcType = ConsoleInput.get_calc_type()
   
    userInput = ConsoleInput.get_user_input()
    print(userInput)
    if (userInput == "quit" or userInput == "q"):
        sys.exit()

    if (calcType == "infix"):
        temp = ReversePolish.shuntParse(userInput)
        result = ReversePolish.exprCalc(temp)
        print(result)
    elif (calcType == "reverse polish"):
        result = ReversePolish.exprCalc(userInput)
