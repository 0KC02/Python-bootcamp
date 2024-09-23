import os
import shutil

# Introduction
print("This program helps you automatically sort files in a directory into categorized folders.")

# Setup
import os

# Getting User Input
directory_path = input("Enter the path to the directory you want to organize: ")
if not os.path.isdir(directory_path):
    print("Invalid directory path. Please try again.")
    exit()

# Mapping Extensions to Folder Names
mapping = {}
while True:
    extension = input("Enter a file extension (or leave blank to finish): ")
    if not extension:
        break
    folder_name = input("Enter the corresponding folder name: ")
    mapping[extension] = folder_name

# Processing the Directory
for root, dirs, files in os.walk(directory_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        file_extension = os.path.splitext(file_name)[1]
        if file_extension in mapping:
            folder_name = mapping[file_extension]
            folder_path = os.path.join(root, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, folder_path)
        else:
            # Handle files without extension or not in mapping
            others_folder_path = os.path.join(root, "Others")
            if not os.path.exists(others_folder_path):
                os.makedirs(others_folder_path)
            shutil.move(file_path, others_folder_path)

# Completion Message
print("File organization complete.")