import time

import numpy as np
import cv2 as cv
from random import randint


class TransformVideo:


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

            # set the color to video_grayscale
            video_grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            grid = self.calc_grid(cols=40, rows=40, video_shape=video_grayscale.shape)
            self.draw_grid(video=video_grayscale, grid=grid)

            cv.imshow('You are so pretty', video_grayscale)
            if cv.waitKey(1) == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

    def calc_grid(self, cols: int, rows: int, video_shape: tuple) -> tuple:
        """
        calc the grid cols and rows
        :param cols:
        :param rows:
        :param video_shape:
        :return:
        """
        height, width = video_shape
        cell_cols = width // cols
        cell_rows = height // rows
        return cell_cols, cell_rows, height, width

    def draw_grid(self, grid: tuple, video):
        """
        draw grid on video
        :param grid:
        :param video:
        :return:
        """
        total_rows = 40
        total_cols = 40
        ascii = ''
        cell_cols, cell_rows, height, width = grid

        # draw the grid
        for col in range(cell_cols, width, cell_cols):
            cv.line(video, (col, 0), (col, height), (255, 0, 0), 1)
        for row in range(cell_rows, height, cell_rows):
            cv.line(video, (0, row), (width, row), (255, 0, 0), 1)

        # calc the cell content
        for row in range(0, total_rows):
            for col in range(0, total_cols):
                pixels: list = []
                for cell_col in range(cell_cols * (1 + col - 1), cell_cols * (1 + col)):
                    for cell_row in range(cell_rows * (1 + row - 1), cell_rows * (1 + row)):
                        pixels.append(video[row, col])
                ascii += f'a'
            ascii += '\n'
        print(ascii)

    def calc_pixel_mean(self, pixels: list) -> int:
        """
        calc pixel mean
        :return:
        """
        total = 0
        for pixel in pixels:
            total = total + pixel

        return total // len(pixels)

    def create_char_dict(self, rate: int, length_char_list: int) -> dict:
        """
        create color slice dict to know which character is for which gray shade
        :param rate:
        :return:
        """
        char: dict = {}
        max_color: int = 255
        char_list: str = '*-/@$<µ%=)&{!?:._+§'

        while max_color > 0:
            max_val: int = max_color - 1 if max_color != 255 else 255
            min_val: int = 0 if max_color - rate < 0 else max_color - rate
            max_color -= rate

            select_char = randint(0, length_char_list - 1)
            char[f'{min_val}-{max_val}'] = char_list[select_char]
            char_list = char_list.replace(char_list[select_char], '')
            print(f'select: {select_char} / list: {char_list}')
        print(char)
        return char
