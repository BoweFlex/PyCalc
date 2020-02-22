import sys
from Calculator import ConsoleInput

def main():
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("Welcome to Jonathan's Calculator program!")
    print("+++++++++++++++++++++++++++++++++++++++++\n")
    
    print("++++Choose quit at any time to exit.+++++\n")
    
    calcType = ConsoleInput.get_calc_type()
    print(calcType)
    sys.exit()
    while (userInput != "quit"):
        userInput = ConsoleInput.get_user_input()
        if (userInput == "quit"):
            sys.exit()

    """ cipherDict = ConsoleInput.get_cipher()
        cipher = cipherDict.get("options").lower()
        #print(cipher)

        if (cipher == "quit"):
        sys.exit()
    
        encryptionDict = ConsoleInput.get_cryption()
        encryption = encryptionDict.get("options").lower()
        #print(encryption)

        if (encryption == "quit"):
            sys.exit()
    
        wordOption = ConsoleInput.get_word(encryption)
        #print(cipher)
        #print(encryption)
        #print(wordOption)
        if (encryption == "encrypt"):
        work = Encrypt(wordOption, cipher)
        print("Your encrypted message is: " + work.get_encryption())
    """
if __name__ == "__main__":
    main()
