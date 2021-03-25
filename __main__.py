from image.Transform import Transform


class App:
    def __init__(self):
        self.__transform = Transform(image_path='img/original/mario.jpg')

    def run(self):
        image_name = 'mario'
        self.__transform.to_greyscale(image_name=image_name, new_width=275, new_height=275)
        self.__transform.to_ascii(image_name=image_name, image_path='img/greyscale')


if __name__ == "__main__":
    app = App()
    app.run()
