from transform.TransformImage import TransformImage


class App:
    def __init__(self, image_path: str):
        self.__transform = TransformImage(image_path=image_path)

    def run(self):
        self.__transform.to_ascii(new_size=(500, 200))


if __name__ == "__main__":
    app = App(image_path='img/original/mario.jpg')
    app.run()
