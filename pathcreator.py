import os

def sysPathCreator(rootFolder):
  # Creates a list of all subfolders
  subFolderList2 = os.listdir(rootFolder)
  subFolderList = subFolderList2

  # Deletes any elements from a list if they are a file not a folder
  subFolderList = [x for x in subFolderList2 if "decap Times.txt" not in x]
  #subFolderList = [x for x in subFolderList if not '.fls' in x] # This deletes anything that isnt .fls file
  

  # This create the full path to each subfolder
  subFolderList2 = []
  for a in subFolderList:
    temp = os.path.join(rootFolder,a)
    subFolderList2.append(temp)

  # How many subfolders in root
  totalSubFolders = len(subFolderList)
  print("Total Sub Folders = " + str(totalSubFolders))

  #firstSubFolderCollection = []
  folderStepper = 0
  for allSubFolders in range(totalSubFolders):
      fileStepper = 0
      # For Every Sub Folder
      file = open(subFolderList2[folderStepper] + ".txt","w")
      for a in range(len(os.listdir(subFolderList2[folderStepper]))):
        # Take the first file name within that sub folder
        indivFile = os.listdir(subFolderList2[folderStepper])
        # Add the Sub Folder Path to the individual file name
        file.write(subFolderList2[folderStepper]+ "\\" + indivFile[fileStepper] + "\n")
        fileStepper = fileStepper + 1
      file.close()
      folderStepper = folderStepper + 1

  # At this point subFolderList2 is a full path not just folder name

  print("Finished creating paths")
  print()
