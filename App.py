from transform.Transform import Transform


class App:
    def __init__(self, image_path: str):
        self.__transform = Transform(image_path=image_path)

    def run(self):
        self.__transform.to_ascii(new_width=500, new_height=200, rate_color=13)


if __name__ == "__main__":
    app = App(image_path='img/original/mario.jpg')
    app.run()
