import os
import shutil

# 1. SETUP: Define the folder to clean
# Use '.' to clean the CURRENT folder where this script is running
directory = "." 

# Define rules: Extension -> Folder Name
rules = {
    ".txt": "Text_Files",
    ".pdf": "PDF_Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".py":  "Python_Scripts"
}

print(f"--- Cleaning {os.getcwd()} ---")

# 2. LOOP: Look at every file in the directory
for filename in os.listdir(directory):
    
    # Skip the script file itself (Don't move me!)
    if filename == "day15_organizer.py":
        continue

    # 3. IDENTIFY: Get the file extension (e.g., .jpg)
    # os.path.splitext("photo.jpg") gives ("photo", ".jpg")
    name, extension = os.path.splitext(filename)
    
    # Check if this extension is in our rules
    if extension in rules:
        folder_name = rules[extension]
        
        # 4. PREPARE: Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Created folder: {folder_name}")

        # 5. ACTION: Move the file
        # shutil.move(source, destination)
        shutil.move(filename, f"{folder_name}/{filename}")
        print(f"Moved: {filename} -> {folder_name}")

print("--- Organization Complete! ---")