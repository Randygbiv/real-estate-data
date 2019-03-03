# this will be the file that does the querying of information for display
from Storage import MongoActions

mongoHelp = MongoActions.mongoHelper()

class QueryData:
    def greeting(self):
        print("Hey there from display query data")

    def queryByZipcode(self, zipC):
        #this gathers the data into a list
        a = mongoHelp.queryDataBy("zipcode", zipC)
        #this declares an empty list to store values in
        b = []
        #not we iterate over those values and store them in the empty list
        for x in a:
            b.append(x)
        return b
    
    def queryBySqFt(self, sqFtO, sqFtT):
        b = []
        squareFootOne = sqFtO - 1
        squareFootTwo = sqFtT + 1
        for x in range(squareFootOne, squareFootTwo):
            a = mongoHelp.queryDataBy("size", x)
            for x in a:
                b.append(x)
        return b

    def queryByRooms(self, numRooms):
        b = []
        a = mongoHelp.queryDataBy("rooms", numRooms)
        for x in a:
            b.append(x)
        return b

    def queryByPrice(self, priceOne, priceTwo):
        b = []
        priceO = priceOne -1
        priceT = priceTwo +1
        for x in range(priceO, priceT):
            a = mongoHelp.queryDataBy("cost", x)
            for x in a:
                b.append(x)
        return b