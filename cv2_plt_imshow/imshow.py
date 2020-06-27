import cv2
import matplotlib.pyplot as plt

def cv2_plt_imshow(image):
    return plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

def plt_format(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)