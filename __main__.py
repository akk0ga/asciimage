from image.Transform import Transform


class App:
    def __init__(self):
        self.__transform = Transform(image_path='img/original/vangog.jpg')

    def run(self):
        image_name = 'vangog'
        self.__transform.to_greyscale(image_name=image_name)
        self.__transform.to_ascii(image_name=image_name, image_path='img/greyscale')


if __name__ == "__main__":
    app = App()
    app.run()
