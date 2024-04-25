import os
import shutil


# Define the path to the directory or folder
path = os.path.join(os.path.expanduser("~"),"Downloads")
print("path:", path)

# Listing the items (files and folders) in directory
contents = os.listdir(path)
print("Contents:")
for item in contents:
    print(item)

# Grouping the files by extensions
print("Grouping the files by extension:") 
def group_files_by_type(path):
    files_by_type = {}

    contents = os.listdir(path)

    for item in contents:
        item_path = os.path.join(path, item)

        if os.path.isfile(item_path):
            _, file_ext = os.path.splitext(item)

        file_ext = file_ext[1:].lower()
        print(file_ext) 

        if file_ext in files_by_type:
            files_by_type[file_ext].append(item)
        else:
            files_by_type[file_ext] = [item]

    return files_by_type


files_by_type = group_files_by_type(path)

for file_type, files in files_by_type.items():
    print(f"{file_type.upper()} files:")
    for file_name in files:
        print(f"- {file_name}")


def create_destination_folders(files_by_type):
    home_path = os.path.expanduser('~')

    for file_type in files_by_type:
        folder_name = file_type.upper()
        folder_path = os.path.join(home_path, folder_name)

        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

def move_files_to_folders(files_by_type, path):
    home_path = os.path.expanduser('~')

    for file_type, files in files_by_type.items():
        for file_name in files:
            src_file_path = os.path.join(path, file_name)
            dest_folder_path = os.path.join(home_path, file_type.upper())

            shutil.move(src_file_path, dest_folder_path)

def main():
    path = os.path.join(os.path.expanduser('~'), "Downloads")
    files_by_type = group_files_by_type(path)
    create_destination_folders(files_by_type)
    move_files_to_folders(files_by_type, path)

    print("Files moved to destination folders successfuly!")

if __name__ == "__main__":
    main()


















