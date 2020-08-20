#!/usr/bin/env python3

from PIL import Image
import os

def fix_images(my_dir, new_dir, file_type, degree, width, height):
    #This module roates image 90 degrees, resize image and change image format
    files = os.listdir(my_dir)
    for f in files:
        image_location = os.path.abspath(os.path.join(my_dir,f))
        base = os.path.splitext(f)[0]
        base = base + file_type
        new_image_location = os.path.abspath(os.path.join(new_dir, base))
        if os.path.isdir(image_location):
            #ignore directories for now.  can be used to extend the filename in the future and make new directories to map original
            pass
        else:
            #process the image
            im = Image.open(image_location)
            new_im = im.rotate(degree).resize((width, height)).convert("RGB").save(new_image_location)


if __name__ == "__main__":
    #state the source and destination of the images and teh new file type
    my_dir = "/home/nicole/Pictures"
    new_dir = "/home/nicole/Pictures/Edited-Pictures"
    file_type = ".jpg"
    #state the degree of rotation and new height and width
    degree = 90
    width = 640
    length = 480

    fix_images(my_dir, new_dir, file_type, degree, width, height)
