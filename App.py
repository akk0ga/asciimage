from transform.TransformImage import TransformImage
from transform.TransformVideo import TransformVideo


class App:
    def __init__(self, image_path: str):
        self.__transform = TransformImage(image_path=image_path)

    def run(self):
        choice: str = input('1 -> image\n2 -> video\nyour choice: ')
        while choice != '1' and choice != '2':
            choice: str = input('1 -> image\n2 -> video\nyour choice: ')

        if choice == '1':
            choice: str = input('want you resize the image ? [y/n]: ')
            while choice != 'y' and choice != 'n':
                choice: str = input('1 -> image\n2 -> video\nyour choice: ')

            if choice == 'y':
                width: str = input('new width: ')
                height: str = input('new height: ')
                self.__transform.to_ascii(new_size=(int(width), int(height)))
            else:
                self.__transform.to_ascii()
        else:
            video = TransformVideo()
            video.to_ascii()


if __name__ == "__main__":
    app = App(image_path='img/original/mario.jpg')
    app.run()
