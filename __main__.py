from image.Image import Image
from image.Transform import Transform


class App:
    def __init__(self):
        self.transform = Transform(image_path='img/greyscale.png')

    def test(self):
        self.transform.to_ascii()


if __name__ == "__main__":
    app = App()
    app.test()
