# https://www.microcenter.com/robots.txt states that this should be fine to scrape their website. If a rep from microcenter wants me to remove it, feel free to contact me and I will remove this
import setup

URL = input("Please enter the Microcenter URL: \n")
print("One moment please...")

print("Installing packages")
setup.install("beautifulsoup4") # beautiful soup 4 to work with html
setup.install("requests") # beautiful soup 4 to generate with http responses
print("Done installing packages")

print("Scraping URL")

setup.run("scraper.py") #running scraper file
print("DONE! Check output.csv")

