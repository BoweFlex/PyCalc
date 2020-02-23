import inquirer

""" Used to get user input """
class ConsoleInput:

    @staticmethod
    def get_calc_type() -> str:
        types = [
                inquirer.List('options',
                    message="What type of calculator would you like to use?",
                    choices=['Infix', 'Reverse Polish', 'Quit'],
                    ),
        ]
        
        typeDict = inquirer.prompt(types)
        return typeDict.get('options').lower()
    
    @staticmethod
    def get_user_input() -> str:
        inputStr = input("Enter whatever you'd like to calculate (Enter \"quit\" to exit): ")
        return inputStr.strip().lower() 
    
    @staticmethod
    def get_further_input() -> str:
        userCont = [
                inquirer.List('options',
                    message="Would you like to calculate another equation?",
                    choices=['Yes', 'No']
                    ),
        ]

        contDict = inquirer.prompt(userCont)
        return contDict.get('options').lower()
