#this will be where we place the main menu
#this will be a class object so that we can call it later

from Helpers import typeHelper, cliHelper
from Prompts import SettingPrompt, DisplayPrompts, DeletePrompt, HelpPromt, GatherPrompt


typeHelp = typeHelper.typesHelper()
cliHelp = cliHelper.Helper()
setPrompt = SettingPrompt.SettingPrompt()
disPrompt = DisplayPrompts.DisplayData()
delPrompt = DeletePrompt.DeletePrompt()
helpPrompt = HelpPromt.HelpPrompt()
gathPrompt = GatherPrompt.GatherPrompt()

class MainPrompt:
    greeting = "Welcome to the real estate CLI, where I parse data to find you deals"
    options = ["gather data", "display data", "delete data", "help", "settings", "exit"]
    
    def mainMenu(self):
        for idx, x in enumerate(self.options):
            print(str(idx + 1) + ") " + x) 
    
    def greetUser(self):
        print(self.greeting)
    
    def makeChoice(self):
        thisChoice = int(input())
        checkType = typeHelp.checkIfNumber(thisChoice)
        if checkType == False:
            print("Enter a number number on the menu")
            return self.makeChoice()
        else:
            if thisChoice < 1 or thisChoice > len(self.options):
                print("On. The. Menu!")
                return self.makeChoice()
            else:
                return self.switchBoard(thisChoice)

    def switchBoard(self, value):
        switchValue = value - 1
        if switchValue == 5:
            return False
        elif switchValue == 4:
            #this will be changed later
            return setPrompt.greetUser()
        elif switchValue == 3:
            return helpPrompt.greetUser()
        elif switchValue == 2:
            return delPrompt.greetUser()
        elif switchValue == 1:
            return disPrompt.greetUser()
        else:
            return gathPrompt.greetUser()
