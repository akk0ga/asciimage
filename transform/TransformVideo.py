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
        :param video_size:
        :return:
        """
        width, height = video.shape

        cols = width // 35
        rows = height // 3

        """
        for col in range(cols, height, cols):
            cv.line(video, (col, 0), (col, height), (255, 0, 0), 1)
        """

        for row in range(rows, height, rows):
            cv.line(video, (0, row), (height, row), (255, 0, 0), 1)
