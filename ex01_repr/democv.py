import cv2

image = cv2.imread('img.jpg', 0)
h, w = image.shape
print (h, w)

for i in range(h):
    for j in range(w):
        if( image[i][j] > 128):
            print ('.', end='')
        else:
            print ('1', end='')
    print('\n', end='')

def horizontal_histogram(image):
    h, w = image.shape
    hist = [0] * h
    for i in range(h):
        for j in range(w):
            if image[i][j] <= 128:
                hist[i] += 1
    return hist

import matplotlib.pyplot as plt

plt.barh(range(h), horizontal_histogram(image))
plt.gca().invert_yaxis()
plt.title("Horizontal Histogram")
plt.show()