from pathcreator import sysPathCreator
from decap import decap
from scanDict import scanDict
from introduction import introduction
from decapFinder import decapFinder
import os
import time


introduction()
decapFinder()

rootFolder = input("Please enter location of the subfolders ")

scanDict(rootFolder)
sysPathCreator(rootFolder)
time.sleep(3)
decap(rootFolder)

print()
print("Recap processing Finished")
input()
