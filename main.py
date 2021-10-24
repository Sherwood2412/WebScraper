import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.parse import urljoin
from urllib import request
from urllib.request import Request, urlopen
import time

url = "https://www.cftc.gov/MarketReports/CommitmentsofTraders/HistoricalCompressed/index.htm"
page = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
r = urlopen(page).read()
time.sleep(2)


doc = BeautifulSoup(r, "html.parser")


Liste = []
for selector in doc.select(".field a"):
    href = selector.get("href")
    filename = urljoin(url, href)
    Liste.append(filename)

    #local_file = "local_copy.txt"
    #request.urlretrieve(filename, "text.xls")

neue_liste = [ x for x in Liste if "_xls_" in x ]

for value in neue_liste:
    try:
        request.urlretrieve(filename, "text.xls")
    except:
        print("Download fehlgeschlagen")
    break