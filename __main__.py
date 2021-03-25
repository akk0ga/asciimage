from image.Transform import Transform


class App:
    def __init__(self):
        self.__transform = Transform(image_path='img/original/test.jpg')

    def run(self):
        image_name = 'test'
        self.__transform.to_greyscale(image_name=image_name, new_width=538, new_height=100)
        self.__transform.to_ascii(image_name=image_name, image_path='img/greyscale')


if __name__ == "__main__":
    app = App()
    app.run()
