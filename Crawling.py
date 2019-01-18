import re
import requests
from bs4 import BeautifulSoup

webURL = 'url'
r = requests.get(webURL)
soup = BeautifulSoup(r.content,'html.parser')
div= soup.find("div", {"class":"listStyle1"})
lis= div.findAll("li")

def getproductinfo(item):
    name = item.find("p",{"class":"pdtName"}).find("em").text
    price=item.find("p",{"class":"price"})
    return {"name":name, "price":price.text.strip()}
for li in lis:
    product_info = getproductinfo(li)
    print("{}@{}".format(product_info['name'],product_info['price']))    