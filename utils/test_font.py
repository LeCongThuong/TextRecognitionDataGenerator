from trdg.generators import GeneratorFromStrings
import glob
import os
from pathlib import Path


def generate_image_from_string_with_font(test_string, font, dest_dir):
    image = next(GeneratorFromStrings([test_string], fonts=[font], size=64, background_type=1, text_color="#000000"))[0]
    _, font_name = os.path.split(font)
    image_path = os.path.join(dest_dir, font_name.split('.')[0] + '.jpeg')
    image.save(image_path)


def main():
    font_dir = '/content/VietnameseOCR/fonts'
    test_string = 'Trường quê sạch và đẹp lắm do bố xây kĩ'
    dest_dir = '/content/results'
    font_list = list(Path(font_dir).rglob("*.[tT][tT][fF]"))
    font_list = [str(font_path) for font_path in font_list]
    for font in font_list:
        generate_image_from_string_with_font(test_string, font, dest_dir)

    print("Num font: ", len(font_list))