import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print("Directory does not exist!")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            ext = file.split('.')[-1] if '.' in file else 'others'
            ext_folder = os.path.join(directory, ext.upper())

            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            
            shutil.move(file_path, os.path.join(ext_folder, file))

    print("Files organized successfully!")

# Usage
organize_files("C:/Users/YourName/Downloads")  # Change path as needed
