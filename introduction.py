import time

def introduction():
    print("""

Hi guys & gals,

thank you for purchasing a copy of the decap batching program,

This program / script does require the following to be able to run: """)
    time.sleep(1)
    print("- decap.exe to be installed here (c:\\Program Files\\Autodesk\\Autodesk ReCap\\)")
    time.sleep(1)
    print("- The user of the machine has Recap Pro subscription")
    time.sleep(1)
    print("- The machine requires to be untouched whilst running")
    time.sleep(1)
    print("- The sub folders holding your scan files must not have anything else stored but your scan files")
    time.sleep(1)
    print("""- The sub folder names must not include spaces or any special character !"£$%^&*() """)
    
    time.sleep(2)

    print("""
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
""")
    time.sleep(2)
    print()
    input("Press enter to continue.....")
    print()
    print()
