from pymongo import MongoClient
#declare client database location
class mongoHelper:
    client = MongoClient('mongodb://localhost:27017/')

    #name the database
    db = client.realEstate

    #name the collection
    listings  = db.listings

    #insert one listing
    def addListing(self, listing):
        self.listings.insert_one(listing)

    #remove many by parameter
    def removeManyListing(self, attr, value):
        self.listings.delete_many({attr: value})

    #query data to the databse
    def queryDataBy(self, keyArg, valArg):
        specListings = self.listings.find({keyArg: valArg})
        return specListings

    #returns a count of a set of documents based on arguments
    def getCount(self, keyArgOne, valArgOne, 
        keyArgTwo, valArgTwo, keyArgThr, valArgThr, keyArgFr, valArgFr):
        countOf = self.db.listings.count_documents({
            keyArgOne: valArgOne,
            keyArgTwo: valArgTwo,
            keyArgThr: valArgThr,
            keyArgFr: valArgFr
        })
        return countOf