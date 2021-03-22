from PIL import Image as Pil_Image


class Image:
    def __init__(self):
        self.__image: Pil_Image

    def _get_info(self) -> tuple[str, tuple, str]:
        """
        get info about the image
        :return:
        """
        file = self.__image
        file_format: str = file.format
        try:
            name: str = file.filename
            # (width, height)
            size: tuple = file.size
            mode: str = file.mode
            return name, size, mode
        except Pil_Image.UnidentifiedImageError:
            print('image isn\'t correct')

    def _show(self) -> None:
        """
        show the image
        :return:
        """
        self.__image.show()

    """
    ===================================
    getter & setter 
    ===================================
    """

    def set_image(self, image_path: str):
        self.__image = Pil_Image.open(image_path)

    def get_image(self):
        return self.__image

    image = property(fget=get_image, fset=set_image)
