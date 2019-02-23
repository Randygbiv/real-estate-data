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

    def queryDataBy(self, keyArg, valArg):
        specListings = self.listings.find({keyArg: valArg})
        return specListings