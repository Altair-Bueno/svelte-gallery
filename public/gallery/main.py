import os
import sys
import json
import shutil
import PIL.Image

FORMAT = "webp"
EXTENSION = "." + FORMAT

# Iterate all files in the current directory, change png to webp 90% quality compression m -6, rename file to lowercase, replace spaces with underscores, delete png
current_dir = os.getcwd()
list_of_files = os.listdir(current_dir)
list_of_dirs = [f for f in list_of_files if os.path.isdir(os.path.join(current_dir, f))]

for dir in list_of_dirs:
    list_of_files = os.listdir(os.path.join(current_dir, dir))
    list_of_images = [f for f in list_of_files if os.path.isfile(os.path.join(current_dir, dir, f)) and f.endswith(".png")]
    for image in list_of_images:
        im = PIL.Image.open(os.path.join(current_dir, dir, image))
        im.convert("RGB").save(os.path.join(current_dir, dir, image.replace(".png", EXTENSION)), FORMAT, quality=80, method=6)
        os.remove(os.path.join(current_dir, dir, image))
        os.rename(os.path.join(current_dir, dir, image.replace(".png", EXTENSION)), os.path.join(current_dir, dir, image.replace(".png", EXTENSION).lower().replace(" ", "_")))
        im.close()

# In the current dir, look at every folder. Every folder contains images, read all images and create a json file array that's:
# [{src: "path/to/image", title: "image title"}, ...]
# We want a differnt json file for each folder, so we can use the folder name as the json file name

# For each directory, get the list of all files in that directory
for dir in list_of_dirs:
    # Get the list of all files in the directory
    list_of_files = os.listdir(os.path.join(current_dir, dir))
    # Get the list of all images in the directory
    list_of_images = [f for f in list_of_files if os.path.isfile(os.path.join(current_dir, dir, f)) and f.endswith(EXTENSION)]
    # Create a json file for this directory in the root directory
    json_file = open(os.path.join(current_dir, dir + ".json"), "w")
    # Create an array of objects
    json_array = []
    # For each image, create an object and add it to the array
    for image in list_of_images:
        json_array.append({"src": "gallery\\" + os.path.join(dir, image), "title": image})
    # Write the json array to the json file
    json.dump(json_array, json_file)
    # Close the json file
    json_file.close()

# Exit the program