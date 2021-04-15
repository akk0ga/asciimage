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
            grid = self.calc_grid(cols=20, rows=20, video_shape=video_grayscale.shape)
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
        total_cols: int = 20
        total_rows: int = 20
        i = 1

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
                # print(f'row: {row} | col: {col} / value: {self.calc_pixel_mean(pixels=pixels)}')

    def calc_pixel_mean(self, pixels: list) -> int:
        """
        calc pixel mean
        :return:
        """
        total = 0
        for pixel in pixels:
            total = total + pixel

        return total // len(pixels)
