import os
import time

def decapFinder():
    print("Checking for decap file location......")
    time.sleep(2)
    while True:
        decapPresent = os.path.isfile("c:\\Program Files\\Autodesk\\Autodesk ReCap\\decap.exe")
        if decapPresent == True:
            print("Success you have decap installed")
            break
        else:
            print("Decap is not installed")
    time.sleep(2)
    print()
    print("Continuing on with decap batcher")
    print()

    input("Press enter to continue.....")
    print()
    print()
