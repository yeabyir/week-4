import os
import shutil
import time

def list_files():
    return os.listdir()

def is_recently_modified(file):
    
    stats = os.stat(file)
    current_time = time.time()
    modification_time = stats.st_mtime
    creation_time = stats.st_ctime
    if current_time - modification_time < 86400 or current_time - creation_time < 86400:
        return True
    else:
        return False

def update_files(files):
    for file in files:
        
        with open(file, 'a') as f:
            
            f.write('\n' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def move_files(files, folder_name):
    for file in files:
        
        shutil.move(file, folder_name)


files = list_files()

recent_files = [file for file in files if is_recently_modified(file)]
update_files(recent_files)
create_folder('last_24hours')
move_files(recent_files, 'last_24hours')
