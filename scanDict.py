import os
def scanDict(rootFolder):
  #rootFolder = ("C:\\Users\\ALS_Surveying\\Desktop\\test folder")

  # Module to build a dictionary, key to hold the sub folder names and the value to hold total scans within the folder

  scanDict = {}

  #subFolderNames = os.listdir(rootFolder)

  # Creates a list of all subfolders
  subFolderList3 = os.listdir(rootFolder)

  # Deletes any elements from a list if they are a file not a folder
  subFolderList = [x for x in subFolderList3 if "." not in x]

   # This create the full path to each subfolder
  subFolderList2 = []
  for a in subFolderList:
    temp = os.path.join(rootFolder,a)
    subFolderList2.append(temp)

##  for b in subFolderList2:
##    print(b)
##  print()

  totalFilesList = []
  stepper = 0
  for counter in range(len(subFolderList2)):
    totalFiles = len(os.listdir(subFolderList2[stepper]))
    stepper = stepper + 1
    totalFilesList.append(totalFiles)

  stepper = 0
  for aa in range(len(subFolderList)):
    scanDict[subFolderList[stepper]] = totalFilesList[stepper]
    stepper = stepper + 1

  timer1 = open(rootFolder + "\\"+ "decap Times.txt","w")
  timer1.write("PROJECT NAME".ljust(30," ") + "SCAN COUNT".rjust(31," ") + "\n")

  for k, v in scanDict.items():
    timer1.write(k.ljust(30, " ") + str(v).rjust(30, " ") + "\n")

  totalScans = 0
  for k, v in scanDict.items():
    totalScans = totalScans + v
  # Calculate Total Scans
  timer1.write(("=" * 55) + "\n")
  timer1.write("Total Scans = " + str(totalScans) + "\n")
  timer1.write("\n")
  timer1.close()

