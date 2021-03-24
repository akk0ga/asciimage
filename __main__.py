from image.Transform import Transform
from image.Image import Image


class App:
    def __init__(self):
        self.__transform = Transform(image_path='img/original/toga.jpg')

    def run(self):
        self.__transform.to_greyscale(image_name='toga')


if __name__ == "__main__":
    app = App()
    app.run()
