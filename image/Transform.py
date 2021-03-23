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

    def to_greyscale(self, image_name: str) -> PilImg:
        """
        convert image from rgb to greyscale
        :param image_name:
        :return:
        """
        img_info = self._get_info()
        img_load = PilImg.open(img_info[0])
        img_greyscale = img_load.convert('L')
        # img_greyscale.save(f'img/{image_name}.png')
        return img_greyscale

    def to_ascii(self):
        """
        TODO
        1- create new image with the size of image to convert
        2- create a list to stock pixel colour with the attribute char
        3- make a loop to check each pixel and if the colour has no char which refer to,
            save it and select char if the pixel is black attribute -> ''
        4- get the pixel position and place char on the new image to the correct coordinate
        :return:
        """
        name, size, mode = self._get_info()
        pixel_color: dict = {}

        # create new image and save it
        new_img = PilImg.new(mode='L', size=size)
        new_img.save('img/new.png')
        new_img.close()

        # get all shade of gray from the original image
        pixel = self.image.getpixel((0, 0))
        print(pixel)

        # check the color for each pixel
        for y in range(0, size[1]):
            for x in range(0, size[0]):
                coordinate: tuple = (x, y)
                pixel = self.image.getpixel(xy=coordinate)

                # stock pixel in the color list and assign ascii to it
                if pixel not in pixel_color and pixel != 0:
                    pixel_color[pixel] = self.__ascii_list[randint(0, len(self.__ascii_list) - 1)]

                print(f'({x}, {y}) -> {pixel}')
        print('CHAR ATTRIBUTION END')
        time.sleep(3)

        # check the pixel color to add the correct character
        new_img = PilImg.open('img/new.png')
        set_font_size = PilFont.truetype('arial.ttf', 1)
        add_ascii = PilDraw.Draw(new_img)
        for y in range(0, size[1]):
            for x in range(0, size[0]):
                coordinate: tuple = (x, y)
                pixel = self.image.getpixel(xy=coordinate)

                # add character
                add_ascii.text(coordinate, pixel_color[pixel], 1000, font=set_font_size)

                print(f'{coordinate} -> {pixel}')
        new_img.save('img/new.png')
        new_img.close()
