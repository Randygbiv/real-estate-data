#this will be where we place the main menu
#this will be a class object so that we can call it later

from Helpers import typeHelper, cliHelper

typeHelp = typeHelper.typesHelper()
cliHelp = cliHelper.Helper()


class MainPrompt:
    greeting = "Welcome to the real estate CLI, where I parse data to find you deals"
    options = ["gather data", "display data", "delete data", "help", "settings", "exit"]
    
    def mainMenu(self):
        for idx, x in enumerate(self.options):
            print(str(idx + 1) + ") " + x) 
    
    def greetUser(self):
        print(self.greeting)

    def makeMainChoice(self):
        choice = cliHelp.makeChoice(self.options)
        return choice
    