import json
from login import *

# Loads JSON file managing exceptions within the 'with' statement
with open('Projects/json_Reader/users.json') as f:
    users = json.load(f)

# Login - 4 max tries
for i in range(0, 4):

    print('Usuário: ')
    login = input()

    print('Senha: ')
    password = input()

    # Calls function to verify credentials and login
    if(loginVerification(login, password, users) != True):
        print('Verification failed. Please try again')
    else:
        print('Verification succeded!\n')

        menu = menuAction()  # Creates menu object from class

        userInput = printsUserMenu()  # Receive user input

        # Loop for multiple actions within the menu - 'x' to exit
        while userInput != 'x':
            os.system('cls')

            if userInput == '1':
                menu.readFile()
                input()
            elif userInput == '2':
                menu.editFile()
            elif userInput == '3':
                menu.deleteFile()
            elif userInput == '4':
                menu.createFile()

            userInput = printsUserMenu()
            os.system('cls')

        break
