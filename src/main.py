import os
import shutil
from PIL import Image
from pillow_heif import register_heif_opener


class ImageConverter:
    def __init__(self, input_dir, output_dir, dest_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.dest_dir = dest_dir

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

    def convert_images(self):
        register_heif_opener()

        for filename in os.listdir(self.input_dir):
            if filename.lower().endswith(".heic"):
                input_path = os.path.join(self.input_dir, filename)

                with Image.open(input_path) as img:
                    output_filename = os.path.splitext(filename)[0] + ".png"
                    output_path = os.path.join(self.output_dir, output_filename)
                    img.save(output_path, "PNG")

                shutil.move(input_path, os.path.join(self.dest_dir, filename))


if __name__ == "__main__":
    input_dir = "images/input_image_heic"
    output_dir = "images/output_image_png"
    dest_dir = "images/already_converted_images"

    converter = ImageConverter(input_dir, output_dir, dest_dir)
    converter.convert_images()

