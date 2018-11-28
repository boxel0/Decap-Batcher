import pyautogui
import os
import time
import datetime

def decap(rootFolder):
    timer1 = open(rootFolder + "\\" + "decap Times.txt","a")
    timer1.write("\n")
    timer1.write("SCAN PROCESSING TIMES:")
    timer1.write("\n")

    # This calculates how many scans are in each folder
    subFolderList = os.listdir(rootFolder)
    subFolderList = [x for x in subFolderList if "." not in x]

    subFolderList2 = []
    for a in subFolderList:
        temp = os.path.join(rootFolder,a)
        subFolderList2.append(temp)

    print("List of SubFolders Ready for Decap Batching")
    for a in subFolderList2:
        print(a)
    print()

    totalFilesList = []
    stepper = 0

    for a in totalFilesList:
        print(a)

    subFolderNames = os.listdir(rootFolder)
    subFolderNames = [x for x in subFolderNames if "." not in x]
    stepper = 0
    now = datetime.datetime.now()

    for eachSubFolder in range(len(subFolderNames)):
        
        #timer1 = open(rootFolder + "\\" + "decap Times.txt","a")
        
        
        # Load Command Prompt
        pyautogui.hotkey("win")
        pyautogui.typewrite("cmd")
        pyautogui.hotkey("enter")
        # Wait for command prompt to open
        time.sleep(1)
        # Locate Decap Location
        pyautogui.typewrite("cd c:\\Program Files\\Autodesk\\Autodesk ReCap\\")
        pyautogui.hotkey("enter")
        # Run Decap with local license
        pyautogui.typewrite("decap.exe  --importWithLicense ")
        #Location to save recap files for subfolder
        pyautogui.typewrite('"' + rootFolder + "\\" + subFolderNames[stepper]+'" ')
        # Name of Recap Files
        pyautogui.typewrite(subFolderNames[stepper])
        # Load and Locate control files
        pyautogui.typewrite(" --controlFile " + '"' + rootFolder + "\\" + subFolderNames[stepper]+".txt")
        time.sleep(1)
        pyautogui.hotkey("enter")
        # Need to add timer to allow the program to finish


        
        now = datetime.datetime.now()
        timer1.write((subFolderNames[stepper] + " - started:".ljust(50)) + (now.strftime("%Y-%m-%d %H:%M").rjust(30)) + "\n")   
        print((subFolderNames[stepper] + " - started:".ljust(50)) , (now.strftime("%Y-%m-%d %H:%M").rjust(30)))
        
        # Add file finder program here
        file = (rootFolder + "\\" + subFolderNames[stepper] + "\\" + subFolderNames[stepper] + ".rcp")
        #print(file)
        while True:
            while not os.path.exists(file):
                time.sleep(1)

            if os.path.isfile(file):
                time.sleep(1)
                break

        now = datetime.datetime.now()
        timer1.write((subFolderNames[stepper] + " - finished:".ljust(50)) + (now.strftime("%Y-%m-%d %H:%M").rjust(30)) + "\n")
        timer1.write("\n")
        print((subFolderNames[stepper] + " - finished:".ljust(50)) , (now.strftime("%Y-%m-%d %H:%M").rjust(30)))
        print()
        #timer1.close()
        stepper += 1
    timer1.close()
