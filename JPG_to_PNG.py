import sys
import os
from PIL import Image
# Ensure that 2 file paths were entered in the terminal
if(len(sys.argv) < 3):
    print('Please try again and enter 2 file paths')
    quit()

# grab the first and second arguments from the Terminal, ensure they aren't blank
jpg_img_folder = sys.argv[1]
png_img_folder = sys.argv[2]

if len(jpg_img_folder) < 1 or len(png_img_folder) < 1:
    print("Please try again and enter 2 file paths.")
    quit()


# ensure that Terminal arguments are in fact directories
if os.path.isdir(jpg_img_folder):
    if not jpg_img_folder.endswith('/'):
        jpg_img_folder += '/'

if not png_img_folder.endswith('/'):
    png_img_folder += '/'

print(
    f'Images in {jpg_img_folder} will be converted and saved to {png_img_folder}')

# check if new folder exists, if not create it
if not (os.path.isfile(png_img_folder) or os.path.exists(png_img_folder)):
    os.mkdir(png_img_folder)

# loop through the entire folder, convert each JPG to PNG and save it in new folder
for jpg_file in os.listdir(jpg_img_folder):
    # Remove extension from name of original file
    filename_without_extension = os.path.splitext(jpg_file)[0]
    with Image.open(f'{jpg_img_folder}{jpg_file}') as img:
        img.save(f"{png_img_folder}{filename_without_extension}.png", "png")
        print(f'{filename_without_extension}.jpg converted.')
