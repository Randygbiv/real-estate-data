#this will be the command to make requests to BS4 and requests
from Helpers import typeHelper
from Scraper import getSite
from Prompts import MainMenu

scrapeHelp = getSite.Site()
typeHelp = typeHelper.typesHelper()

class GatherPrompt:
    greeting = "This is where we'll gather data, it will take prompts"
    options = ['gather data', 'exit']
    warning = "There is nothing to show here, move along"

    def greetUser(self):
        print(self.greeting)
    
    def displayOptions(self):
        for idx, x in enumerate(self.options):
            print(str(idx + 1) + ") " + x)
    
    def makeChoiceInternal(self):
        choice = int(input())
        if typeHelp.checkIfNumber(choice) == False:
            print("enter a number")
            return(self.makeChoiceInternal())
        else:
            if choice - 1 > len(self.options):
                print("make a real choice")
            elif choice == 0:
                return self.subMenu()
            else:
                return 1
                
    def subMenu(self):
        zipC = input("Enter the zipcode you want to search around: ")
        units = input("Enter the unit of measurement you want to search[mile/km]: ")
        dist = input("Enter the distance you want to search around this zip: ")
        ownShip = input("Enter the type of ownership ['rent'/'own']: ")
        if units.lower() != "mile" or units.lower() != "km":
            print("unit must be either mile or km")
            return self.subMenu()
        elif ownShip.lower() != "rent" or ownShip.lower() != "km":
            print("type of ownership must be either 'rent' or 'own'.")
            return self.subMenu()
        else:
            scrapeHelp.getCodesAndCities(zipC, dist, units, "json")
            scrapeHelp.getHtmlDocs(ownShip)
            scrapeHelp.scrapeIt()
            return 1