# Decap-Batcher
Autodesk Recap Decap Batching Script

Hey Guys,
This script works with Autodesk Decap not Recap!
Decap was a program built alongside recap PRO, which allowed you to run Recap without the GUI within command prompt

Decap batcher does require PYAUTOGUI to be installed
Its built with Python 3.xxx

This is my first program so be kind

compile.py - basically in my run / start file

introduction.py - talks about how the script works:
HOW IT WORKS
--------------------------------
Decap batcher runs by first scanning your sub folders for the scan files and creating a list of all there paths,
once this is finished you will notice a .txt file per sub folder.

Then the decap batcher will open a command prompt and automatically load it with the required text to start decap
including the location of the files. This will start the decap processing for the first subfolder.

Once the first sub folder is finished, which is detected by the creatuon of the last file (.rcp), decap batcher
wil automatically start the next subfolder and so on.

***************************************************************************************
Please leave this program to run by itself as it needs full control of your machine!
***************************************************************************************

decapFinder.py - Will check to see if you have access to recap pro and that decap is installed in the default location:
c:\\Program Files\\Autodesk\\Autodesk ReCap\\decap.exe

decap-batcher will ask for the root folder, which holds all the subfolders, each subfolder will be created into a recap project

scanDict.py - this creates a text file, in the root folder depicting the projects to be created and how many files in each project

pathCreator.py - creates the a text file per project, holding the exact location of every scan for the project !important!

decap.py - this opens decap.exe, by using PYAUTOGUI and loads in the text file which holds all the information to run a batch project
