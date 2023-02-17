import os
import shutil
from PIL import Image
from pillow_heif import register_heif_opener

input_dir = "images/input_image_heic"
output_dir = "images/output_image_png"
dest_dir = "images/already_converted_images"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".HEIC") or filename.endswith(".heic"):

        register_heif_opener()
        with Image.open(os.path.join(input_dir, filename)) as img:
            output_filename = os.path.splitext(filename)[0] + ".png"
            output_path = os.path.join(output_dir, output_filename)
            img.save(output_path, "PNG")
            shutil.move(os.path.join(input_dir, filename), os.path.join(dest_dir, filename))
