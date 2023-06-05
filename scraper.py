# https://www.microcenter.com/robots.txt states that this should be fine to scrape their website. If a rep from microcenter wants me to remove it, feel free to contact me and I will remove this
import setup

URL = input("Please enter the Microcenter URL: \n")
print("One moment please...")

print("Installing packages")
#setup.install("beautifulsoup4") # beautiful soup 4 to work with html
#setup.install("requests") # beautiful soup 4 to generate with http responses
print("Done installing packages")

print("Scraping URL")
from bs4 import BeautifulSoup
import requests
import csv

file = open('output.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Item', 'Price', 'CPU', 'Ram', 'Storage'])


page_to_scrape = requests.get(URL) #REQUEST WEBPAGE AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser') #USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE

quotes = soup.findAll('span', attrs={'class':'text'}) #FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
#AND STORE THE LIST AS A VARIABLE

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
#AND STORE THE LIST AS A VARIABLE
authors = soup.findAll('small', attrs={"class":"author"})

#LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
#AND PRINT AND FORMAT THE RESULTS
for quote, author in zip(quotes, authors):
    
    writer.writerow([quote.text, author.text]) #WRITE EACH ITEM AS A NEW ROW IN THE CSV

file.close() #CLOSE THE CSV FILE


print("DONE! Check output.csv")