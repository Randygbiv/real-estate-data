from Scraper import getSite
from Helpers import typeHelper

types = typeHelper.typesHelper()
reqs = getSite.Site()

reqs.getCodesAndCities('27028', '20', 'mile', 'json')
reqs.getHtmlDocs("rent")
reqs.scrapeIt()

