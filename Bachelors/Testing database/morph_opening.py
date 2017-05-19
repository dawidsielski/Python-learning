import cv2
import numpy as np
import os

kernel = np.ones((5,5),np.uint8)

def show_image(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)
print(os.listdir())

valid = [name for name in os.listdir() if ".png" in name]

img = cv2.imread(valid[0],0)
show_image(img)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
show_image(opening)