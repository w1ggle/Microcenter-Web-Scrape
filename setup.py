# using this way because it is officially supported. See https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program
import subprocess

def install():
    if:
        #asd
    exception:
        subprocess.run(["python", "-m", "pip", "install", "beautifulsoup4"])  # beautiful soup 4 to work with html
        subprocess.run(["python", "-m", "pip", "install", "requests"]) #  beautiful soup 4 to work with http

def run(file): # deprecated
    subprocess.run(["python", file])