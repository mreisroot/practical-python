from os import remove
from os.path import exists

file_name = "new_file"

if exists(file_name):
    remove(file_name)
