# using this way because it is officially supported. See https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program
import subprocess

def install(package):
    subprocess.run(["python", "-m", "pip", "install", package])

def run(file): # deprecated
    subprocess.run(["python", file])