import sys
import os
from PIL import Image

# grab the first and second arguments from the Terminal
from_file = sys.argv[1]
to_file = sys.argv[2]

# ensure that Terminal is in fact a file path
if not from_file.endswith('/'):
    from_file += '/'

if not to_file.endswith('/'):
    to_file += '/'

print(f'Images in {from_file} will be converted and saved to {to_file}')

# check if new folder exists, if not create it
if not (os.path.isfile(to_file) or os.path.exists(to_file)):
    os.mkdir(to_file)

# loop through the entire folder, convert each JPG to PNG and save it in new folder
for filename in os.listdir(from_file):
    # Remove extension from name of original file
    clean_name = os.path.splitext(filename)[0]
    with Image.open(f'{from_file}{filename}') as img:
        img.save(f"{to_file}{clean_name}.png", "png")
        print(f'{clean_name}.jpg converted.')
