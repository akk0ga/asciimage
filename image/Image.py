from PIL import Image as Pil_Image


class Image:
    def __init__(self):
        self.__image: Pil_Image

    def _get_info(self) -> dict:
        """
        get info about the image
        :return:
        """
        file = self.__image
        try:
            name: str = file.filename
            size: tuple = file.size
            mode: str = file.mode
            return {
                'name': name,
                'size': size,
                'mode': mode
            }
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

    def set_image(self, image_path: str) -> None:
        """
        set and load image
        :param image_path:
        :return:
        """
        self.__image = Pil_Image.open(image_path)

    def get_image(self) -> None:
        """
        get image
        :return:
        """
        return self.__image

    image = property(fget=get_image, fset=set_image)
