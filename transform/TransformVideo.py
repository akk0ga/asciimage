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
            self.draw_grid(cols=20, rows=20, video=video_grayscale)

            cv.imshow('video', video_grayscale)
            if cv.waitKey(1) == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()

    def draw_grid(self, cols: int, rows: int, video):
        """
        draw grid on video
        :param cols:
        :param rows:
        :param video:
        :return:
        """
        mean: list = []
        height, width = video.shape
        total_cols = width // cols
        total_rows = height // rows

        for col in range(total_cols, width, total_cols):
            cv.line(video, (col, 0), (col, height), (255, 0, 0), 1)

        for row in range(total_rows, height, total_rows):
            cv.line(video, (0, row), (width, row), (255, 0, 0), 1)

        for col in range(0, total_cols):
            for row in range(0, total_rows):
                mean.append(video[row, col])

                # uncomment to check if take only one cell
                # cv.line(video, (col, row), (col, row), (255, 0, 0), 1)
