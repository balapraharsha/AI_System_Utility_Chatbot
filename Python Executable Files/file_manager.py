import os
import shutil

# ===== File & Folder Operations =====
def create_file(file_name):
    with open(file_name, 'w') as f:
        f.write("")
    print(f"File '{file_name}' created.")

def delete_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"File '{file_name}' deleted.")
    else:
        print(f"File '{file_name}' does not exist.")

def create_folder(folder_name):
    os.makedirs(folder_name, exist_ok=True)
    print(f"Folder '{folder_name}' created.")

def delete_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
        print(f"Folder '{folder_name}' deleted.")
    else:
        print(f"Folder '{folder_name}' does not exist.")

# Placeholders for other commands
def rename_file(file_name, new_name): pass
def rename_folder(folder_name, new_name): pass
def move_file(file_name, dest_folder): pass
def move_folder(folder_name, dest_folder): pass
def copy_file(file_name, dest_folder): pass
def copy_folder(folder_name, dest_folder): pass
def list_files(folder_name): pass
def search_files(extension, folder_name): pass
def show_file_details(file_name): pass
def count_files(folder_name): pass
