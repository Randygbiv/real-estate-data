#this will be used to call functions that will help the cli

#dependencies
import os
import platform
from Helpers import typeHelper
from Prompts import SettingPrompt, DisplayPrompts, DeletePrompt, HelpPromt, GatherPrompt

typeHelp = typeHelper.typesHelper()
setPrompt = SettingPrompt.SettingPrompt()
disPrompt = DisplayPrompts.DisplayData()
delPrompt = DeletePrompt.DeletePrompt()
helpPrompt = HelpPromt.HelpPrompt()
gathPrompt = GatherPrompt.GatherPrompt()

#class
class Helper:

    #function call for clear
    def clear(self):
        if(platform.system() == 'Linux'):
            os.system('clear')
        elif(platform.system() == 'Windows'):
            os.system('cls')
        else:
            #because fuck apple
            print("You're probably running some Apple Machine, I don't +"
                    "write code for panzies")
            print("If you're not using an Apple OS, please contact me")
    
    #function call for empty lines
    def addLines(self, x):
        for a in range(0, x):
            print(" ")
    
    #this will print a please wait in the middle of the screen
    def pleaseWait(self):
        self.clear()
        self.addLines(3)
        print("Please wait while processing the request")
        self.addLines(3)

    def makeChoice(self, options):
        thisChoice = int(input())
        checkType = typeHelp.checkIfNumber(thisChoice)
        if checkType == False:
            print("Enter a number number on the menu")
            return self.makeChoice(options)
        else:
            if thisChoice < 1 or thisChoice > len(options):
                print("On. The. Menu!")
                return self.makeChoice(options)
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