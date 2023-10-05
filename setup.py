# using this way because it is officially supported. See https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program
import subprocess

packageList = ["beautifulsoup4", "requests", "selenium"]
# beautiful soup 4 to work with html
# requests to work with http
# selenium to work with multiple pages

def install():
        for package in packageList:
                try:
                        __import__(package)
                except ImportError:
                        subprocess.run(["python", "-m", "pip", "install", package])  
                        
def run(file): # deprecated
    subprocess.run(["python", file])