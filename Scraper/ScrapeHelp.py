#this is the class that will handle parsing the data
from bs4 import BeautifulSoup
from Helpers import typeHelper
from Storage import MongoActions

typeHelp = typeHelper.typesHelper()
mongoHelp = MongoActions.mongoHelper()

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
        self.packStorage()

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
        self.links.append(link['href'])
        a = typeHelp.mutateType(typeHelp.checkNone(size, "content"), "int")
        b = typeHelp.mutateType(typeHelp.checkNone(price, "content"), "int")
        c = self.stripZip(zipCode.text)
        d = typeHelp.mutateType(typeHelp.checkNone(room, "none"), "int")
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
    def packStorage(self):
        for idx, zipC in enumerate(self.zipCodes):
            listing = {
                "zipcode": self.zipCodes[idx],
                "link": self.links[idx],
                "size": self.floorSizes[idx],
                "price": self.cost[idx],
                "rooms": self.rooms[idx]
            }
            mongoHelp.addListing(listing)
