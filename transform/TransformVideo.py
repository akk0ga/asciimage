import numpy as np
import cv2 as cv
from random import randint


class TransformVideo:
    __char_list: str = '*-/@$<µ%=)&{!?:._+§'

    def webcam(self):
        cap = cv.VideoCapture(0)

        # check if already open
        if not cap.isOpened():
            print("Cannot open camera")
            exit()

        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            # Our operations on the frame come here
            # set the color to video_grayscale
            video_grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            cv.imshow('video', video_grayscale)
            self.to_ascii(video=video_grayscale)
            if cv.waitKey(1) == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

    def to_ascii(self, video):
        rows, cols = video.shape
        new_width: int = 150
        new_height: int = 200

        # set the char list for color_slice
        color_slice = self.__create_char_dict(rate=20, length_char_list=len(self.__char_list))
        char = ''

        for col in range(0, cols):
            for row in range(0, rows):
                color = video[row, col]
                for key in color_slice:
                    val_min, val_max = key.split('-')
                    if int(val_min) <= color <= int(val_max):
                        char_select = color_slice[f'{val_min}-{val_max}'] if row != rows - 1 else f'{color_slice[f"{val_min}-{val_max}"]}\n'
                        char = char + char_select
            if col == cols - 1:
                char = char + '\n'

        print(char)

    def __create_char_dict(self, rate: int, length_char_list: int) -> dict:
        """
        create color slice dict to know which character is for which gray shade
        :param rate:
        :return:
        """
        char: dict = {}
        max_color: int = 255

        while max_color > 0:
            max_val: int = max_color - 1 if max_color != 255 else 255
            min_val: int = 0 if max_color - rate < 0 else max_color - rate
            max_color -= rate

            select_char = randint(0, length_char_list - 1)
            char[f'{min_val}-{max_val}'] = self.__char_list[select_char]
            self.__char_list.replace(self.__char_list[select_char], '')
        return char
