#this will be used to call functions that will help the cli

#dependencies
import os
import platform

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