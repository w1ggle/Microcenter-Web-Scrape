from bs4 import BeautifulSoup
import requests
import csv
from setup import URL 

file = open('output.csv', 'w')
writer = csv.writer(file)
writer.writerow(['Item', 'Price', 'CPU', 'Ram', 'Storage'])

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get(URL)
#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
#AND STORE THE LIST AS A VARIABLE
quotes = soup.findAll('span', attrs={'class':'text'})

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'AUTHOR'
#AND STORE THE LIST AS A VARIABLE
authors = soup.findAll('small', attrs={"class":"author"})

#LOOP THROUGH BOTH LISTS USING THE 'ZIP' FUNCTION
#AND PRINT AND FORMAT THE RESULTS
for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)
    #WRITE EACH ITEM AS A NEW ROW IN THE CSV
    writer.writerow([quote.text, author.text])
#CLOSE THE CSV FILE
file.close()