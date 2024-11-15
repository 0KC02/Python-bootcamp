import os
import shutil

# Mapping of file extensions to folder names
FILE_TYPE_MAPPING = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Pictures': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Programs': ['.exe', '.msi'],
    'Others': []
}

def organize_files(directory_path):
    # Create category folders if they don't exist
    for category in FILE_TYPE_MAPPING.keys():
        category_folder = os.path.join(directory_path, category)
        os.makedirs(category_folder, exist_ok=True)
    
    # Loop through each file in the directory
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Get the file extension
        _, extension = os.path.splitext(filename)
        
        # Find the folder for this file type
        moved = False
        for category, extensions in FILE_TYPE_MAPPING.items():
            if extension.lower() in extensions:
                destination_folder = os.path.join(directory_path, category)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                moved = True
                break
        
        # If no matching extension was found, move to 'Others'
        if not moved:
            shutil.move(file_path, os.path.join(directory_path, 'Others', filename))

    print("Files organized successfully.")

# Example usage
directory_path = "C:/Users/Owner/Downloads"
organize_files(directory_path)
