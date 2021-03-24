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
        self.__ascii_list = '@*/.,%$()&+-^_:<>=;!?'

    def to_greyscale(self, image_name: str, path: str = 'img/greyscale') -> None:
        """
        resize convert and save RGB image to resize grayscale image
        :param path:
        :param image_name:
        :return:
        """
        resize = self.image.resize((800, 500))
        img_greyscale = resize.convert('L')
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

    def to_ascii(self, new_image_name: str = 'new', save_path: str = 'img/ascii',
                 greyscale_path: str = 'img/greyscale') -> None:
        """
        create and save new image in ascii art
        :return:
        """
        # load and get greyscale image and info
        self.image = f'{greyscale_path}/{new_image_name}.png'
        image_size: tuple = self._get_info()['size']

        # get pixel color
        pixel_color = self.get_pixel_color(image_size=image_size)

        # create new empty image
        print(pixel_color)

        # load the image create before to draw on
        new_img = PilImg.open(f'{save_path}/{new_image_name}.png')
        set_font_size = PilFont.truetype('arial.ttf', 1)
        add_ascii = PilDraw.Draw(new_img)

        for y in range(0, image_size[1]):
            for x in range(0, image_size[0]):
                coordinate: tuple = (x, y)
                pixel = self.image.getpixel(xy=coordinate)

                # add character
                if pixel in pixel_color and pixel > 10:
                    add_ascii.text(coordinate, pixel_color[pixel], 1000, font=set_font_size)
                    print(f'{x},{y} -> {pixel_color[pixel]}')

        new_img.save(f'{save_path}/{new_image_name}.png')
        new_img.close()
