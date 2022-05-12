import skimage
import cv2 
import numpy as np 

def subdivided(frame):
    shape = np.shape(frame)
    a = 0
    b = 0
    list = []
    list_cord = []
    for val1 in range(int(shape[0]/8), shape[0], int(shape[0]/8)):
        b = 0
        for val2 in range(int(shape[1]/8), shape[1], int(shape[1]/8)):
            list.append(frame[a:val1, b:val2, :])
            list_cord.append((a, val1, b, val2))
            b += int(shape[1]/8)
        a += int(shape[0]/8)
    return list, list_cord

def cord_division(frame, list):
    squares = []
    for val in list:
        squares.append(frame[val[0]:val[1], val[2]:val[3], :])
    return squares
