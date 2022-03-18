import json
import os


def loginVerification(user, password, loginInfo):
    if((user == loginInfo['user']) and (password == loginInfo['password'])):
        return True
    else:
        return False


# Prints menu options
def printsUserMenu():
    print('What would you like to do next?')
    print('1-Read file\n2-Edit File\n3-Delete file\n4-Create new JSON file\n')
    print("'x' to exit")
    choice = input()

    return choice


class menuAction:

    def __init__(self) -> None:
        pass

    def readFile(self):

        with open('Projects/json_Reader/users.json') as f:
            self.info = json.load(f)

        print(json.dumps(self.info, indent=2, sort_keys=True))

    def editFile(self, path):
        osCommandString = "notepad.exe " + path
        os.system(osCommandString)
        # somehow open a text editor from here or allow editing on the terminal

    def deleteFile(self, path):
        if os.path.exists(path):
            os.remove(path)
        else:
            print(
                "The file doesn't exists in this directory.\nPlease check the path you've given and try again.")

    def createFile(self):
        print('Name of the file - with extension: ')
        self.fileName = input()

        print('Path where the file will be created: ')
        self.path = input()

        if os.path.exists(self.path+self.fileName):
            print('The file already exists, please write a different file name.')
        else:
            with open(self.path+self.fileName, 'x') as f:
                pass
