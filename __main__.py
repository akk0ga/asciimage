from image.Transform import Transform
from image.Image import Image


class App:
    def __init__(self):
        self.__transform = Transform(image_path='img/original/smiley.jpg')

    def run(self):
        image_name = 'smiley'
        self.__transform.to_greyscale(image_name=image_name)
        self.__transform.to_ascii(new_image_name=image_name)


if __name__ == "__main__":
    app = App()
    app.run()
