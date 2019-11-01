

import os

import time

path = "C:\\Users\\dogma\\OneDrive\\Desktop\\HTML Documents\\The-Tech-Academy-Basic-Python-Projects\\A\\"

dirs = os.listdir(path)

for file in dirs:
    if file.endswith(".txt"):
        txt_files = os.path.join(path,file)
        mTime = time.localtime(os.path.getmtime(path))
        fTime = time.strftime("%m/%d/%Y, %H:%M:%S", mTime)
        print("File Name:", txt_files,"Modified:", fTime)

