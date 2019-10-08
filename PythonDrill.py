

import os

import time

path = "C:\\Users\\dogma\\OneDrive\\Desktop\\HTML Documents\\The-Tech-Academy-Basic-Python-Projects\\A\\"

dirs = os.listdir(path)

for file in dirs:
    if file.endswith(".txt"):
        print(file)

path1 = os.path.join(path, "Hello.txt")

mod_time1 = os.path.getmtime(path1)

local_time1 = time.ctime(mod_time1)
print(local_time1)

path2 = os.path.join(path, "World.txt")

mod_time2 = os.path.getmtime(path2)

local_time2 = time.ctime(mod_time2)
print(local_time2)
