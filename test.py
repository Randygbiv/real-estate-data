from Scraper import getSite
from Displayers import Displayer

queryHelp = Displayer.QueryData()
scrapeHelp = getSite.Site()

# scrapeHelp.getCodesAndCities("27028", "50", "mile", "json")
# scrapeHelp.getHtmlDocs("rent")
# scrapeHelp.scrapeIt()

#a = queryHelp.queryByZipcode("27028")
a = queryHelp.queryBySqFt(600, 900)
print(a)