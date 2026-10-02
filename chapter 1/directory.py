import os

directory_path = '/vs code'

try:
    print(f"Scanning directory: {os.path.abspath(directory_path)}\n")
    
    # os.scandir yields DirEntry objects, which are highly efficient
    with os.scandir(directory_path) as entries:
        print("📁 Directories:")
        # Loop through first to print folders
        for entry in entries:
            if entry.is_dir():
                print(f"  {entry.name}/")
                
    # Resetting the scanner requires calling it again if we loop twice
    with os.scandir(directory_path) as entries:
        print("\n📄 Files:")
        # Loop through to print files
        for entry in entries:
            if entry.is_file():
                print(f"  {entry.name}")
                
except FileNotFoundError:
    print(f"Error: '{directory_path}' could not be found.")

    # yesma ai use vako xa hai 