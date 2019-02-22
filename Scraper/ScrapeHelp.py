#this is the class that will handle parsing the data
from bs4 import BeautifulSoup
from Helpers import typeHelper

typeHelp = typeHelper.typesHelper()

class Scrapper:

    zipCodes = []
    links = []
    cost = []
    rooms = []
    floorSizes = []

    #this will be a new test parse data
    def parseData(self, element):
        self.removeLists()
        soup = BeautifulSoup(element, 'html.parser')
        listing = soup.find_all("div", itemprop="offers")
        for list in listing:
            link = list.find("a", class_="js-item-title") #this needs to be str
            size = list.find("meta", itemprop="floorSize") #this needs to be int
            price = list.find("meta", itemprop="price") #this also needs to be int
            zipCode = list.find("h5", itemprop="address")
            room = list.find("span", itemprop="numberOfRooms") #needs to be int
            self.dataHelper(link, size, price, zipCode, room)
            
    #this will add to the floor list
    def checkNone(self, elm, typeOfTag):
        if elm == None:
            return 'None'
        else:
            if typeOfTag == "none":
                return elm.text
            else:
                return elm[typeOfTag]
    
    #Mutates the type of element so that it can be parsed correctly.
    def mutateType(self, elm, typeOfData):
        if elm == "None":
            return elm
        else:
            if typeOfData == 'int':
                return int(elm)
            else:
                return str(elm)

    #this will help with mutating zipcodes to the proper format
    def stripZip(self, elm):
        newZip = elm[2:7]
        for x in range(5):
            a = newZip[x]
            if typeHelp.tryParseInt(a) != False:
                return newZip
            else:
                return 00000

    #this gets called by the function parseData
    def dataHelper(self, link, size, price, zipCode, room):
        self.links.append(link)
        a = self.mutateType(self.checkNone(size, "content"), "int")
        b = self.mutateType(self.checkNone(price, "content"), "int")
        c = self.stripZip(zipCode.text)
        d = self.mutateType(self.checkNone(room, "none"), "int")
        self.floorSizes.append(a)
        self.cost.append(b)
        self.zipCodes.append(c)
        self.rooms.append(d)

    #this will clear the list after each iteration so that we're not adding the
    #values to our database over and over
    def removeLists(self):
        self.zipCodes = []
        self.cost = []
        self.rooms = []
        self.links = []
        self.floorSizes = []
    #this will take each part of the arrays to an object and send it to the database
    #def packStorage(self):
