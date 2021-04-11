import numpy as np
import cv2 as cv


class TransformVideo:
    __char_list: str = '*-/@$<µ%=)&{!?:._+§'

    def __init__(self):
        pass

    def to_ascii(self):
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
            # set the color to gray
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            # Display video
            cv.imshow('you in ascii... You\' pretty !', gray)

            # if put on q stop all
            if cv.waitKey(1) == ord('q'):
                break
            # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()
