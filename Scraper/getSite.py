#this file will contain the class that gets the request information
import requests
from bs4 import BeautifulSoup
import json

class Site:

    baseUrl = 'https://homes.trovit.com/'
    zipcodes = []
    webContent = []
    cities = []
    states = []
    content = []
    apiKey = "hCT4e2DiYyQhrfnBlM32tAay5KMoCAgmNsVMyi4cfxFIxIw0qcCjRllAK22EjrV1"
    
    ##this is a test function
    def hello(self):
        print("Hello from Scrapper class")

    #this places all the zipcodes in an area and their cities in lists
    def getCodesAndCities(self, zipc, dist, units, frmat):
        a = requests.get("https://www.zipcodeapi.com/rest/" + self.apiKey
            + "/radius." + frmat + "/" + zipc + "/" + dist + "/" + units)
        b = json.loads(a.content)
        c = b.get("zip_codes")
        for each in c:
            x = each.get("zip_code")
            y = each.get("city")
            z = each.get("state").lower()
            self.zipcodes.append(x)
            self.cities.append(y)
            self.states.append(z)
    
    #this places all the html documents into an array
    def getHtmlDocs(self, rentOwn):
        for idx, each in enumerate(self.zipcodes):
            city = self.changeTwoToOne(self.cities[idx])
            if rentOwn.lower() == "own":
                a = requests.get(self.baseUrl + city + "-" + self.states[idx]
                    + "-" + self.zipcodes[idx])
                if a.status_code == 200:
                    self.webContent.append(a.content)
            elif rentOwn.lower() == "rent":
                a = requests.get(self.baseUrl + "for-rent-" + city + "-" +
                    self.states[idx] + "-" + self.zipcodes[idx])
                if a.status_code == 200:
                    self.webContent.append(a.content)

    
    #above function was getting to big so this will handle some things
    def changeTwoToOne(self, value):
        a = value.split()
        if len(a) > 1:
            b = "-".join(a)
            return b
        else:
            return value

    #now to parse through the data and use it with bs4
