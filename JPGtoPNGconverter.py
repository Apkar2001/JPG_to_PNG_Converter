import sys
import os
from pathlib import Path
from PIL import Image

folder = sys.argv[1]
new_folder = sys.argv[2]

isExist = os.path.exists(new_folder)

def converting():
    for i in os.listdir(folder):
        if i.endswith(".jpg"):
            fn = i.split(".jpg")[0]
            img = Image.open(os.path.join(" !ENTER YOUR ROUTE WHERE YOU KEEP IMAGES! ", i))
            img.save(f'{new_folder}{fn}.png', 'png')
        else:
            continue
            
def new_file():
    os.makedirs(new_folder)

if not isExist:
    new_file()
    converting()
else:
    converting()

# Plan

# 1. grab first and second argument

# 2. check if new/ exists, if not create it

# 3. loop throw image folder,

# 4. convert images to png

# 5. save to the new folder