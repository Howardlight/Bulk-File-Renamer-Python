"""File Renamer"""
# a script that changes the names in a folder and organizes them from 1 to n
# New names include: ImageN.png and VideoN.mp4
# TODO: Clean the code, IE refactor it

import os
import shutil


def NamechangerImg(FileName, ImageNum, extensionType):

    # Create a new name for the looped-to file.
    New_name = str(FileName) + str(ImageNum) + str(extensionType)

    # Create 2 paths, one to the file and one to its new name.
    # This is to simplify the Shutil command.
    Current_file_name = os.path.join(Select_a_path, filename)
    New_file_name = os.path.join(Select_a_path, New_name)


    # This guarantees that the shutil module will not override
    # existing files with similar names
    while os.path.exists(str(New_file_name)):
        ImageNum = ImageNum + 1
        New_name = str(FileName) + str(ImageNum) + str(extensionType)
        New_file_name = os.path.join(Select_a_path, New_name)


    shutil.move(Current_file_name, New_file_name)


def NamechangerVid(FileName, VidNum, extensionType):

    # Same Function as the NumChangerImg but for videos
    New_name = str(FileName) + str(VidNum) + str(extensionType)

    Current_file_name = os.path.join(Select_a_path, filename)
    New_file_name = os.path.join(Select_a_path, New_name)

    while os.path.isfile(str(New_file_name)):
        VidNum = VidNum + 1
        New_name = str(FileName) + str(VidNum) + str(extensionType)
        New_file_name = os.path.join(Select_a_path, New_name)

    shutil.move(Current_file_name, New_file_name)


Select_a_path = input("Please select a path:")

# Main loop: searches for all the folders, subfolders and filenames in a Path.
try:
    for folderName, subfolders, filenames in os.walk(Select_a_path):
        # loop of the filenames
        ImageNum, VidNum = 1, 1
        for filename in filenames:
            Check_extension = str(filename)

            # Looks for images with the following extensions.
            if Check_extension.lower().endswith((".png", ".jpg", ".jpeg")):

                # Loops each time to increase the file number.

                # Sets what the FileName is
                FileName = "Image"

                # Sets what the extensionType is
                extensionType = ".jpg"

                """WARNING: while i have fixed the override issue,
                   I'm still not sure that it is safe or that the
                   issue won't surface again."""
                # Excecutes the function
                NamechangerImg(FileName, ImageNum, extensionType)

            # Looks for Videos with the following extensions.
            elif Check_extension.lower().endswith((".mp4", ".webm", ".mov")):

                # Loops each time to increase the file number.

                # Sets what the FileName is
                FileName = "Video"

                # Sets what the extensionType is
                extensionType = ".mp4"

                # Excecutes the function
                NamechangerVid(FileName, VidNum, extensionType)

            else:
                continue

    print("Done!")

# The try command is so if an error takes place, the rest of the code
# (if i write more code after it) doesn't break with it.
except Exception as err:
    # Prints an error if that happens.
    print("An exception happened: " + str(err))
