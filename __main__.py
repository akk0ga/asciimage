from Image import Image


class App:
    def __init__(self):
        self.image = Image(image_path='img/test.jpg')

    def test(self):
        self.image.get_info()
        image_convert = self.image.greyscale()


if __name__ == "__main__":
    app = App()
    app.test()
