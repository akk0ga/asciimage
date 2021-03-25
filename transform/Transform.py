from PIL import Image as PilImg


class Transform:
    def __init__(self, image_path: str):
        self.__image: PilImg = PilImg.open(image_path)

    def __to_greyscale(self, new_height: int, new_width: int) -> str:
        """
        resize convert and save RGB transform to resize grayscale transform
        if you want to resize the transform you have to precise new width AND new height
        :param new_width:
        :param new_height:
        :return:
        """
        # keep aspect ratio
        if new_height != 0 and new_width != 0:
            width = int(new_height / new_height * new_width)
            resize = self.__image.resize((width, new_height))
            img_greyscale = resize.convert('L')
        else:
            img_greyscale = self.__image.convert('L')
        img_greyscale.save(f'img/grayscale.png')
        return f'img/grayscale.png'

    def to_ascii(self, new_width: int = 0, new_height: int = 0) -> None:
        """
        create ascii image
        :return:
        """
        self.__image = PilImg.open(self.__to_greyscale(new_width=new_width, new_height=new_height))

        # color_slice list
        color_slice = {
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
