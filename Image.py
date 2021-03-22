from PIL import Image as Pil_Image


class Image:
    def __init__(self, image_path: str):
        self.__image: Pil_Image = Pil_Image.open(image_path)

    def get_info(self) -> None:
        """
        get info about the image
        :return:
        """
        file = self.__image
        file_format: str = file.format

        if file.format == 'JPEG' or file.format == 'PNG' or file.format == 'JPG':
            name: str = file.filename
            # (width, height)
            size: tuple = file.size
            mode: str = file.mode
            print(f'-----image info-----\n'
                  f'name: {name}\n'
                  f'size: width {size[0]} / height {size[1]}\n'
                  f'mode: {mode}\n'
                  f'file_format: {file_format}\n'
                  f'--------------------')
        else:
            print(f'file_format isn\'t correct {file_format}')

    def show(self):
        self.__image.show()
