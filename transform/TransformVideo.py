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

            cv.imshow('video', video_grayscale)
            if cv.waitKey(1) == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

    def calc_grid(self, cols: int, rows: int, video_shape: tuple) -> tuple:
        height, width = video_shape
        total_cols = width // cols
        total_rows = height // rows
        return total_cols, total_rows, height, width

    def draw_grid(self, grid: tuple, video):
        """
        draw grid on video
        :param grid:
        :param video:
        :return:
        """
        mean: list = []
        total_cols, total_rows, height, width = grid

        for col in range(total_cols, width, total_cols):
            cv.line(video, (col, 0), (col, height), (255, 0, 0), 1)

        for row in range(total_rows, height, total_rows):
            cv.line(video, (0, row), (width, row), (255, 0, 0), 1)

        for col in range(total_cols, total_cols+total_cols):
            for row in range(0, total_rows):
                mean.append(video[row, col])
                # uncomment to check if take only one cell
                cv.line(video, (col, row), (col, row), (255, 0, 0), 1)

        # calc mean
        total = 0
        for value in mean:
            total = total+value

        total = total//len(mean)
        print(total)
