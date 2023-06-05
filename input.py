URL = input("Please enter the Microcenter URL: \n")

print("URL received, one moment please...")

import setup
# beautiful soup 4 to work with htmls
setup.install("beautifulsoup4")

# beautiful soup 4 to generate with http responses
setup.install("requests")