import requests
from bs4 import BeautifulSoup
import unicodedata

url = "https://homes.trovit.com/for-rent-mocksville-nc-27028"

response = requests.get(url)

content = response.content

soup = BeautifulSoup(content, 'html.parser')

prices = soup.find_all("span", {"class": "amount"})
newPrices = []
newNewPrices = []

for x in prices:
    newPrices.append(x.text)

for x in newPrices:
    y = x.strip("$")
    z = y.replace(",", "")
    a = int(z)
    newNewPrices.append(a)

print(newNewPrices)