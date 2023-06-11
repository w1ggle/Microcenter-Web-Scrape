# https://www.microcenter.com/robots.txt states that this should be fine to scrape their website. If a rep from microcenter wants me to remove it, feel free to contact me and I will remove this
import setup

#URL = input("Please enter the Microcenter URL: \n")
URL = "https://www.microcenter.com/search/search_results.aspx?N=4294967288&NTK=all&sortby=pricelow&storeid=075" 
print("One moment please...")

print("Installing packages")
#setup.install()
print("Done installing packages")

print("Scraping URL")
from bs4 import BeautifulSoup
import requests
import csv

#file = open('output.csv', 'w')
#writer = csv.writer(file)
#writer.writerow(['Product', 'Price', 'CPU', 'Ram', 'Storage'])
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0", 
    "method": "GET",
    "mode": "cors"
}
#"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0", 
#"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0",
page_to_scrape = requests.get(URL,headers=headers) 
soup = BeautifulSoup(page_to_scrape.text, 'html.parser') 
products = soup.findAll('li', attrs={"class":"product_wrapper"})

for product in products:
    print((product.findAll("a")[1].get("data-brand")) + " " + (product.findAll("a")[1].get("data-name").replace('&quot','"'))) #brand and model
    print(product.find("li", attrs={"class":"spec_1 primary"}).text) #cpu
    print(product.find("li", attrs={"class":"spec_2 primary"}).text) #ram
    print(product.find("li", attrs={"class":"spec_3 primary"}).text) #storage
    print("--------------------------")
with open('output2.txt', 'a') as f:
    f.write(str(products)) 
#prices = soup.findAll('small', attrs={"class":"author"})
#cpus = soup.findAll('small', attrs={"class":"author"})
#rams = soup.findAll('small', attrs={"class":"author"})
#storages = soup.findAll('small', attrs={"class":"author"})

#for quote, author in zip(quotes, authors):
#    writer.writerow([quote.text, author.text]) 

#file.close() 


print("DONE! Check output.csv")