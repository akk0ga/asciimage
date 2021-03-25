from image.Transform import Transform


class App:
    def __init__(self, image_path: str, grayscale_image_name: str = 'new'):
        self.__grayscale_image_name = grayscale_image_name
        self.__transform = Transform(image_path=image_path)

    def run(self):
        self.__transform.to_ascii(image_name=self.__grayscale_image_name, image_path='img/greyscale')


if __name__ == "__main__":
    app = App(image_path='img/original/mario.jpg', grayscale_image_name='mario')
    app.run()
