from image.Transform import Transform


class App:
    def __init__(self):
        self.transform = Transform(image_path='img/greyscale.png')

    def test(self):
        self.transform.to_greyscale(path='img', image_name='greyscale2')


if __name__ == "__main__":
    app = App()
    app.test()
