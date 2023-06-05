# using this way because it is officially supported. See https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program

import subprocess
#import sys

def install(package):
    #subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    subprocess.run(["python", "-m", "pip", "install", package])

def run(file):
    subprocess.run(["python", file])