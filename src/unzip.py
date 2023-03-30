import zipfile
import os
from os.path import exists


directory="data/raw/"

for filename in os.listdir(directory):
    if filename.endswith(".zip"):
        print(filename)
        try:
            with zipfile.ZipFile(directory+filename) as z:
                z.extractall()
                print("Extracted all")
        except:
            print("Invalid file")