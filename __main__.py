from image.Transform import Transform
from image.Image import Image


class App:
    def __init__(self):
        self.__transform = Transform(image_path='img/greyscale/greyscale.png')
        self.__image = Image()

    def run(self):
        self.__image.image = 'img/toga.jpg'
        self.__transform.to_greyscale(path='img', image_name='greyscale')


if __name__ == "__main__":
    app = App()
    app.run()
