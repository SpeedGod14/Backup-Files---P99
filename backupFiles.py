import os
import shutil
source = input("Enter your source folder ")
destination = input("Enter your destination folder ")
listOfFiles = os.listdir(source)
for file in listOfFiles:
    shutil.copy((source+"/"+file), destination+"/"+file)