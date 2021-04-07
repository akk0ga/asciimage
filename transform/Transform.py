from PIL import Image as PilImg
from random import randint


class Transform:
    __char_list: str = '*-/@$<µ%=)&{!?:._+§'

    def __init__(self, image_path: str):
        self.__image: PilImg = PilImg.open(image_path)

    def __to_grayscale(self, new_size: tuple) -> str:
        """
        resize convert and save RGB transform to resize grayscale transform
        if you want to resize (new_width, new_height)
        return the path of img grayscaled\n
        :param new_size: tuple
        :return: str
        """
        path = 'img/grayscale.png'
        # keep aspect ratio
        if new_size is not None:
            new_width, new_height = new_size
            width = int(new_height / new_height * new_width)
            resize = self.__image.resize((width, new_height))
            img_greyscale = resize.convert('L')
        else:
            img_greyscale = self.__image.convert('L')

        img_greyscale.save(path)
        return path

    def to_ascii(self, rate_color: int = 0, new_size: tuple = ()) -> None:
        """
        create ascii image\n
        :return: None
        """
        length_char_list = len(self.__char_list)

        # transform image to b&w
        self.__image = PilImg.open(self.__to_grayscale(new_size=new_size))

        # set the char list for color_slice
        if rate_color <= length_char_list and rate_color != 0:
            color_slice = self.__create_char_dict(rate=rate_color, length_char_list=length_char_list)
        else:
            color_slice = self.__create_char_dict(rate=length_char_list, length_char_list=length_char_list)

        # write color_slice in text file
        with open('draw.txt', 'w') as data:
            for y in range(0, self.__image.height):
                for x in range(0, self.__image.width):
                    color = self.__image.getpixel((x, y))
                    for key in color_slice:
                        val_min, val_max = key.split('-')
                        if int(val_min) <= color <= int(val_max):
                            char = color_slice[
                                f'{val_min}-{val_max}'] if x != self.__image.width - 1 else f'{color_slice[f"{val_min}-{val_max}"]}\n'
                            data.write(char)
            data.close()
            self.__image.close()

    def __create_char_dict(self, rate: int, length_char_list: int) -> dict:
        """
        create color slice dict to know which character is for which gray shade
        :param rate:
        :return:
        """
        char: dict = {}
        max_color: int = 255

        while max_color > 0:
            max_val: int = max_color - 1 if max_color != 255 else 255
            min_val: int = 0 if max_color - rate < 0 else max_color - rate
            max_color -= rate

            select_char = randint(0, length_char_list - 1)
            char[f'{min_val}-{max_val}'] = self.__char_list[select_char]
            self.__char_list.replace(self.__char_list[select_char], '')
        return char
