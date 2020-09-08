#! python3
"""File Renamer"""
# a script that changes the names in a folder and organizes them from 1 to n
# New names include: ImageN.png and VideoN.mp4
# TODO: Clean the code, IE refactor it

import os
import shutil

class ChangeName():
    def __init__(self, FileName, extensionType, FileNum):
        # A class which contains the function that can change the names of files in a
        #    certain folder.
        self.FileName = str(FileName)
        self.extensionType = str(extensionType)
        self.FileNum = FileNum

    def Namechanger(self, FileName, extensionType, FileNum):

        # Create a new name for the looped-to file.
        New_name = str(FileName) + str(FileNum) + str(extensionType)

        # Create 2 paths, one to the file and one to its new name.
        # This is to simplify the Shutil command.
        Current_file_name = os.path.join(Select_a_path, filename)
        New_file_name = os.path.join(Select_a_path, New_name)


        # This guarantees that the shutil module will not override
        # existing files with similar names
        while os.path.exists(str(New_file_name)):
            FileNum = FileNum + 1
            New_name = str(FileName) + str(FileNum) + str(extensionType)
            New_file_name = os.path.join(Select_a_path, New_name)


        shutil.move(Current_file_name, New_file_name)

# Create 2 instances of the class, one for video, one for Images.
ImageNameChanger = ChangeName('IMG', '.jpg', 1)
VideoNameChanger = ChangeName('VID', '.mp4', 1)


Select_a_path = input("Please select a path:")

# Main loop: searches for all the folders, subfolders and filenames in a Path.
# TODO: Expand the script to NOT change jpegs, png to a certain extension type
# TODO: Display the file names being changed in terminal(CMD, Powershell)
# TODO: Offer the user the ability to Specify a first name for the new names(IMG, Images, Vid, VID ect..)
try:
    for folderName, subfolders, filenames in os.walk(Select_a_path):

        # loop of the filenames
        # NOTE: everytime a new instance is created, you have to add a new variable related to it here.
        # NOTE NOTE: This might be obselete with classes having their own preset variable. 
        ImageNum, VidNum = 1, 1

        for filename in filenames:
            Check_extension = str(filename)

            # Looks for images with the following extensions.
            if Check_extension.lower().endswith((".png", ".jpg", ".jpeg")):

                """WARNING: while i have fixed the override issue,
                    I'm still not sure that it is safe or that the
                    issue won't surface again."""

                # Excecutes the Image instance of the function
                ImageNameChanger.Namechanger('IMG', '.jpg', 1)

            # Looks for Videos with the following extensions.
            elif Check_extension.lower().endswith((".mp4", ".webm", ".mov")):

                # Excecutes the Video instance of the function
                VideoNameChanger.Namechanger('VID', '.mp4', 1)

            else:
                continue

    print("Done!")

# The try command is so if an error takes place, the rest of the code
# (if i write more code after it) doesn't break with it.
except Exception as err:
    # Prints an error if that happens.
    print("An exception happened: " + str(err))
