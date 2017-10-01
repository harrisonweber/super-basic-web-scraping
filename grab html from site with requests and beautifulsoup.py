#import stuff
import requests
from bs4 import BeautifulSoup
#scrape html
req = requests.get('https://harrisonweber.com/') #insert your own url in quotes
soup = BeautifulSoup(req.text, "lxml")
#print it
print(soup)