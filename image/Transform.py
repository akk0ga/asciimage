from image.Image import Image


class Transform(Image):
    def __init__(self, image_path: str):
        super().__init__()
        self.image = image_path

    def __to_greyscale(self, image_name: str, new_height: int = 0, new_width: int = 0,
                       path: str = 'img/greyscale') -> None:
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

    def to_ascii(self, image_name: str, image_path: str) -> None:
        """
        use Courier font
        create and save new image in color_slice art
        :return:
        """
        self.__to_greyscale(image_name=image_name)
        # load and get greyscale image and info
        self.image = f'{image_path}/{image_name}.png'

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
            for y in range(0, self.image.height):
                for x in range(0, self.image.width):
                    color = self.image.getpixel((x, y))
                    for key in color_slice:
                        val_min, val_max = key.split('-')
                        if int(val_min) <= color <= int(val_max):
                            char = color_slice[f'{val_min}-{val_max}'] if x != self.image.width - 1 else f'{color_slice[f"{val_min}-{val_max}"]}\n'
                            data.write(char)
            data.close()
