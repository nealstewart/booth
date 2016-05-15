# import the necessary packages
from collections import deque
import math
import time

import imutils
import numpy as np

import cv2

AREA = 1000
QUEUE_SIZE = 10

def main():
    camera = cv2.VideoCapture(0)
    time.sleep(0.25)

    myqueue = deque(list(), QUEUE_SIZE)

    last_frame = None
    while camera.isOpened():
        grabbed, frame = camera.read()

        if not grabbed:
            break

        frame = imutils.resize(frame, width=AREA)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if last_frame is None:
            last_frame = gray
            continue

        frame_delta = cv2.absdiff(last_frame, gray)
        last_frame = gray

        myqueue.append(frame_delta)

        movement_only = np.zeros(last_frame.shape, dtype=np.uint8)

        for idx, delta in enumerate(myqueue):
            adjusted_delta = cv2.multiply(delta, 1 / (len(myqueue) - idx))
            movement_only = cv2.add(movement_only, adjusted_delta)

        lowres = imutils.resize(movement_only, width=250)
        
        print(get_ascii_of_image(lowres))

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()



"""
8-bit ascii lookup table
"""
ASCII_LOOKUP = {
    0: ".",
    1: ":",
    2: "*",
    3: "I",
    4: "V",
    5: "F",
    6: "N",
    7: "M"
}

def get_ascii_of_image(image):
    """
    Outputs the string representation of an image
    Assumes the image is B&W
    """
    ascii_output = ""
    for y_coord in range(0, len(image)):
        for x_coord in range(0, len(image[y_coord])):
            ascii_output = ascii_output + get_ascii_char(image[y_coord][x_coord])

        ascii_output = ascii_output + "\n"

    return ascii_output

def get_ascii_char(num):
    """
    Converts an 8 bit integer representation of brightness to an ascii character
    """
    return ASCII_LOOKUP[math.floor(num / 32)]

main()
