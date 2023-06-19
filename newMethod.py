# https://www.microcenter.com/robots.txt states that this should be fine to scrape their website. If a rep from microcenter wants me to remove it, feel free to contact me and I will remove this
import setup

#URL = input("Please enter the Microcenter URL: \n") #TODO make url have default case
URL = "https://www.microcenter.com/search/search_results.aspx?N=4294967288+4294818548+4294819270+4294819837+4294814254+4294814572+4294805366+4294814062+4294816439+4294818783&NTK=all&sortby=pricelow&rpp=96&storeID=075"

print("Installing packages") #TODO make setup an if statement
#setup.install()
print("Done installing packages")

print("Scraping URL")
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/99.0", 
    "method": "GET"
}
page_to_scrape = requests.get(URL,headers=headers) 
soup = BeautifulSoup(page_to_scrape.text, 'html.parser') 

import csv

file = open('test.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Brand', 'Model', 'CPU', 'Ram', 'Storage', 'Price'])


products = soup.findAll('li', attrs={"class":"product_wrapper"}) #TODO check if faster using div class="results_right"

for product in products:
    brand = product.findAll("a")[1].get("data-brand") #brand and model
    model = product.findAll("a")[1].get("data-name").replace('&quot','"') 

    colorIndex = model.rfind('-')
    color = model[colorIndex+2:]
    index = model.rfind('"')
    model = model[:index+1]

        
    fullDetails = product.find("div", attrs={"class":"h2"}).text.split("; ") #getting specs
    for detail in fullDetails[1:]:
        if(detail.find("Processor") > -1):
            cpu = detail
        elif(detail.find("RAM") > -1):
            ram = detail
        elif(detail.find("Solid State Drive") > -1):
            storage = detail
        else:
            gpu = detail




    
    priceOpenBox = product.find("div", attrs={"class":"clearance"}) #going to open box 
    priceOpenBoxIndex = priceOpenBox.text.find("$") #checking if open box exists
    
    if (priceOpenBoxIndex == -1):
        price = (product.find("span", attrs={"itemprop":"price"}).text) #normal price
        openBoxStatus = ""
    else:
        price = (priceOpenBox.text[priceOpenBoxIndex:]) #open box
        openBoxStatus = "x"

    writer.writerow([brand, model, cpu, ram, storage,gpu, price,openBoxStatus,color]) 




file.close() 
print("DONE! Check output.csv")