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
        pixels: list = []
        total_cols: int = 20
        total_rows: int = 20
        i = 1

        cell_cols, cell_rows, height, width = grid

        for col in range(cell_cols, width, cell_cols):
            cv.line(video, (col, 0), (col, height), (255, 0, 0), 1)

        for row in range(cell_rows, height, cell_rows):
            cv.line(video, (0, row), (width, row), (255, 0, 0), 1)

        while i <= total_cols:
            j = 1
            while j <= total_rows:
                print(i)
                for col in range(cell_cols * i-1, cell_cols * i):
                    for row in range(cell_rows * j-1, cell_rows * j):
                        pixels.append(video[row, col])
                        # uncomment to check if take only one cell
                        # cv.line(video, (col, row), (col, row), (255, 0, 0), 1)
                j += 1
            i += 1

        self.calc_pixel_mean(pixels=pixels)

    def calc_pixel_mean(self, pixels: list):
        """
        calc pixel mean
        :return:
        """
        total = 0
        for pixel in pixels:
            total = total + pixel

        total = total // len(pixels)
        print(total)
