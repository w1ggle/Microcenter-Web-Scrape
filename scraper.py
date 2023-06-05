# https://www.microcenter.com/robots.txt states that this should be fine to scrape their website. If a rep from microcenter wants me to remove it, feel free to contact me and I will remove this
import setup

URL = input("Please enter the Microcenter URL: \n")
print("One moment please...")

print("Installing packages")
#setup.install()
print("Done installing packages")

print("Scraping URL")
from bs4 import BeautifulSoup
import requests
import csv

file = open('output.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Product', 'Price', 'CPU', 'Ram', 'Storage'])

page_to_scrape = requests.get(URL) 
soup = BeautifulSoup(page_to_scrape.text, 'html.parser') 

products = soup.findAll('span', attrs={'class':'text'}) 
prices = soup.findAll('small', attrs={"class":"author"})
cpus = soup.findAll('small', attrs={"class":"author"})
rams = soup.findAll('small', attrs={"class":"author"})
storages = soup.findAll('small', attrs={"class":"author"})

for quote, author in zip(quotes, authors):
    writer.writerow([quote.text, author.text]) 

file.close() 


print("DONE! Check output.csv")