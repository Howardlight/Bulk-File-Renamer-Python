#! python3
"""File Renamer"""
# a script that changes the names in a folder and organizes them from 1 to n
# TODO: Clean the code, IE refactor it

import os
import shutil

def main():
    # Main class
    class ChangeName():
        def __init__(self, FileName, extensionType, FileNum):
            # A class which contains the function that can change the names of files in a
            #    certain folder.
            self.FileName = str(FileName)
            self.extensionType = str(extensionType)
            self.FileNum = FileNum

        def Namechanger(self):

            # Create a new name for the looped-to file.
            New_name = str(self.FileName) + str(self.FileNum) + str(self.extensionType)

            # Create 2 paths, one to the file and one to its new name.
            # This is to simplify the Shutil command.
            Current_file_name = os.path.join(Select_a_path, filename)
            New_file_name = os.path.join(Select_a_path, New_name)


            # This guarantees that the shutil module will not override
            # existing files with similar names
            while os.path.exists(str(New_file_name)):
                self.FileNum = self.FileNum + 1
                New_name = str(self.FileName) + str(self.FileNum) + str(self.extensionType)
                New_file_name = os.path.join(Select_a_path, New_name)


            shutil.move(Current_file_name, New_file_name)
            logInfo = f'Renamed {filename} to {New_name}'
            logfile.write(logInfo + '\n')

            print(logInfo)


    # Create all necessary classes
    JPGNameChanger = ChangeName('JPG-', '.jpg', 1)
    PNGNameChanger = ChangeName('PNG-', '.png', 1)
    JPEGNameChanger = ChangeName('JPEG-', '.jpeg', 1)

    GIFNameChanger = ChangeName('GIF-', '.gif', 1)
    MP4NameChanger = ChangeName('MP4-', '.mp4', 1)
    WEBMNameChanger = ChangeName('WEB-', '.webm', 1)
    MOVNameChanger = ChangeName('MOV-', '.mov', 1)


    Select_a_path = input("Please select a path:")

    # Log file
    Lognumber = 1
    logname = f'Log-{Lognumber}.txt'

    while os.path.exists(str(logname)):
        Lognumber += 1
        logname = f'Log-{Lognumber}.txt'
    
    logfile = open(logname, 'w')
    logfile.write(f'Path to folder: {Select_a_path}')
    logfile.write('\n')
    logfile.write('\n')


    # Main loop: searches for all the folders, subfolders and filenames in a Path.
    try:
        for _, _, filenames in os.walk(Select_a_path): # folderName, subfolders, filenames is the default

            for filename in filenames:
                Check_extension = str(filename)

                # IMAGES
                if Check_extension.lower().endswith(".jpg"):
                    # For JPGs
                    JPGNameChanger.Namechanger()

                elif Check_extension.lower().endswith(".png"):                    
                    # For PNGs
                    PNGNameChanger.Namechanger()


                elif Check_extension.lower().endswith(".jpeg"):
                    # For JPEGs
                    JPEGNameChanger.Namechanger()


                # VIDEOS
                elif Check_extension.lower().endswith((".mp4", ".webm", ".mov")):
                    # For MP4s
                    MP4NameChanger.Namechanger()

                elif Check_extension.lower().endswith(".webm"):
                    # For WEBMs
                    WEBMNameChanger.Namechanger()
                
                elif Check_extension.lower().endswith(".mov"):
                    # For MOVs
                    MOVNameChanger.Namechanger()

                elif Check_extension.lower().endswith(".gif"):
                    # For GIFs
                    GIFNameChanger.Namechanger()

        logfile.close()
        print(f'Changes saved to {logname}')
        print("Done!")

    except Exception as err:
        # Prints an error if that happens.
        print("An exception happened: " + str(err))

if __name__ == '__main__':
    main()