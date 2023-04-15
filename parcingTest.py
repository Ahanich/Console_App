import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)

sup_ejje = BeautifulSoup(response.text, "lxml")

data = sup_ejje.find_all("div", class_="col-lg-4 col-md-6 mb-4")

for i in data:

    name = i.find("h4", class_="card-title").text.replace("\n", '')
    price = i.find("h5").text.replace("\n", '')
    url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
    print()
    print(name, "\n" ,price, "\n" , url_img)
