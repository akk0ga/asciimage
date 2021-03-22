from PIL import Image as PilImg
from image.Image import Image


class Transform(Image):
    def __init__(self, image_path: str):
        super().__init__()
        self.image = image_path
        self.__ascii_list = '@*/.,%$()&+-^_:'

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
        name, size, mode = self._get_info()
        pixel_color: list = []

        # if image is not greyscale
        image = self.image if mode != 'L' else self.to_greyscale(self.image)
        coordinate = x, y = (0, 0)
        pixel = image.getpixel(coordinate)

        # get pixel from image
        print(pixel)

        # change pixel color
        for height in range(0, size[1]):
            for width in range(0, size[0]):
                image.getpixel((width, height)) = 0
