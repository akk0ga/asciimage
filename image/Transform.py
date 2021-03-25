from PIL import Image as PilImg
from PIL import ImageDraw as PilDraw
from PIL import ImageFont as PilFont

from image.Image import Image
from random import randint

import time


class Transform(Image):
    def __init__(self, image_path: str):
        super().__init__()
        self.image = image_path
        self.__ascii_list = '+:/-=@$_'

    def to_greyscale(self, image_name: str, new_height: int = 0, new_width: int = 0, path: str = 'img/greyscale') -> None:
        """
        resize convert and save RGB image to resize grayscale image
        if you want to resize the image you have to precise new width AND new height
        :param new_width:
        :param new_height:
        :param path:
        :param image_name:
        :return:
        """
        # keep aspect ratio
        if new_height and new_width != 0:
            width = int(new_height / new_height * new_width)
            resize = self.image.resize((width, new_height))
            img_greyscale = resize.convert('L')
        else:
            img_greyscale = self.image.convert('L')
            print('not transformed')

        img_greyscale.save(f'{path}/{image_name}.png')

    def get_pixel_color(self, image_size: tuple):
        """
        get pixel color from
        :return:
        """
        pixel_color = {}

        for y in range(0, image_size[1]):
            for x in range(0, image_size[0]):
                coordinate: tuple = (x, y)
                pixel = self.image.getpixel(xy=coordinate)

                # stock pixel in the color list and assign ascii to it
                if pixel not in pixel_color and pixel > 10:
                    pixel_color[pixel] = self.__ascii_list[randint(0, len(self.__ascii_list) - 1)]
        return pixel_color

    def to_ascii(self, image_name: str, image_path: str) -> None:
        """
        use Courier font
        create and save new image in ascii art
        :return:
        """
        # load and get greyscale image and info
        self.image = f'{image_path}/{image_name}.png'
        image_size: tuple = self._get_info()['size']
        print(image_size)

        # ascii list
        ascii = {
            '0-29': ' ',
            '30-59': '+',
            '60-89': ':',
            '90-119': '/',
            '120-149': '-',
            '150-179': '=',
            '180-209': '@',
            '210-239': '$',
            '240-255': '_'
        }

        # write ascii in text file
        with open('draw.txt', 'w') as data:
            for y in range(0, image_size[1]):
                for x in range(0, image_size[0]):
                    coordinate = (x, y)
                    color = self.image.getpixel(coordinate)
                    for key in ascii:
                        new_key = key.replace('-', ' ')
                        val_min, val_max = new_key.split()
                        if int(val_min) <= color <= int(val_max):
                            if x != image_size[0]-1:
                                data.write(ascii[f'{val_min}-{val_max}'])
                            else:
                                char = ascii[f'{val_min}-{val_max}']
                                data.write(f'{char}\n')
            data.close()
