import os
import random
import shutil
import glob

source = input("Enter the source directory: ")
dest = input("Enter the Destination directory: ")

pathchooser = rf'{source}'
files = os.listdir(pathchooser)
randomfile = random.choice(files)

dir_path = rf'{dest}\**/'
file_path = glob.glob(dir_path, recursive=True)
randomdir = random.choice(file_path)

path = rf'{source}\{randomfile}'
sendpath = rf'{randomdir}/{randomfile}'
shutil.copy(path, sendpath)

print("Copied file to random directory completed!")
