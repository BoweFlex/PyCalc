import sys
from Calculator import ConsoleInput

def main():
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to Jonathan's Calculator program!")
    print("+++++++++++++++++++++++++++++++++++++++++\n")
    
    print("++++Choose quit at any time to exit.+++++\n")
    
    calcType = ConsoleInput.get_calc_type()
    print(calcType)
   
    userInput = ""
    while (userInput != "quit"):
        userInput = ConsoleInput.get_user_input()
        print(userInput)
        if (userInput == "quit" or userInput == "q"):
            sys.exit()
        elif (calcType == "infix"):
            pass

if __name__ == "__main__":
    main()
