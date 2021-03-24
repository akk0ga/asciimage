from image.Transform import Transform
import asyncio


class App:
    def __init__(self):
        self.__transform = Transform(image_path='img/original/smiley.jpg')

    async def run(self):
        image_name = 'smiley'
        self.__transform.to_greyscale(image_name=image_name)
        self.__transform.to_ascii(new_image_name=image_name)


if __name__ == "__main__":
    app = App()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run())
    loop.close()
