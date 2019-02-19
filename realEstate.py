#for now this will be where we test the other classes
#this will be where we call the other functions

from Prompts import MainMenu
from Prompts import HelpPromt

mainMenu = MainMenu.MainPrompt()
helpPrompt = HelpPromt.HelpPrompt()

running = True

while running == True:
    mainMenu.greetUser()
    mainMenu.mainMenu()
    choice = mainMenu.makeChoice()
    if choice == False:
        running = False