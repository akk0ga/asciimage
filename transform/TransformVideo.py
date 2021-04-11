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

            cv.putText(gray, 'OpenCV', (10, 200), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)
            # Display video
            print(gray[0, 0])
            cv.imshow('video', gray)
            img = np.zeros((512, 512, 3), np.uint8)
            cv.imshow('image', img)
            # ==================================
            # get pixel
            # ==================================
            # access image property

            # if put on q stop all
            if cv.waitKey(1) == ord('q'):
                break
            # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()
