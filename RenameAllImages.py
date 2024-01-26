import os
import imagehash
from PIL import Image
import pytesseract
# Setup tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\tcamp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
base_path = os.getcwd()
folder_path_for_personalities = base_path + r"\Personalities\Headshots"

# List of hair colours
hair_colours = []
# List of hair lengths
hair_lengths = []

# List of all horses recorded 
horses = []

# List all images in directory
path = f"{base_path}\\UnprocessedHorses"
all_files = os.listdir(path)
# Split into pairs - horse stats and rarity
paired_files = {}
list_of_keys = []
odd = True
oddCounter = 0
counter = 0
for file in all_files:
    oddCounter += 1
    if oddCounter % 2 == 0:
        odd = False
    else:
        odd = True
    # If there is a file ending in _stats, make that the key and change 
    # the _stats to _rarity for the value
    if "_stats" in file:
        value = file.replace("_stats","_rarity")
        paired_files[file] = value
        #Add the key to a list
        list_of_keys.append(file)
    
    if odd:
        counter += 1
        # name stats
        name = f"{path}\\{counter}_stats.png"
    else:
        # name rarity
        name = f"{path}\\{counter}_rarity.png"
    currentName = f"{path}\\{file}"
    os.rename(currentName, name)
    print(file)
    