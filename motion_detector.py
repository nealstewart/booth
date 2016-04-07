# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2
import numpy as np
from collections import deque

AREA = 1000
QUEUE_SIZE = 10


def doCameraStuff():
    camera = cv2.VideoCapture(0)
    time.sleep(0.25)

    myqueue = deque(list(), QUEUE_SIZE)

    lastFrame = None
    while True:
        (grabbed, frame) = camera.read()
        text = "Unoccupied"

        if not grabbed:
            break

        frame = imutils.resize(frame, width=AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if lastFrame is None:
            lastFrame = gray
            continue

        frameDelta = cv2.absdiff(lastFrame, gray)
        lastFrame = gray

        myqueue.append(frameDelta)

        s = np.zeros(lastFrame.shape, dtype=np.uint8)

        for idx, delta in enumerate(myqueue):
            s = cv2.add(s, delta)

        cv2.imshow("Frame Delta", s)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

doCameraStuff()
