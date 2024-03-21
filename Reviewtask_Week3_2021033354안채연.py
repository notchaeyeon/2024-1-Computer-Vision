import cv2 as cv
import numpy as np
import matplotlib.pylab as plt

#Task1_implement a 5x5 box filtering using integral image
img = cv.imread('lenna.png', cv.IMREAD_GRAYSCALE)
if img is None:
    print("file not found")
    
    
bImg = cv.blur(img, (5,5))    

sumimg = cv.integral(img)
bImg2 = np.zeros((img.shape[0], img.shape[1]))


img_boxFilter = cv.boxFilter(img, -1, (50,50))

titles = ['Original Image','Blurred', 'With IntegralImg', 'img_boxFilter']
images = [img, bImg, bImg2, img_boxFilter]
cv.imshow('winname', img_boxFilter)
'''
for i in range(3):
    cv.imshow(titles[i], images[i])
    '''

#Task2_Otsu Binarization with Soccer.jpg
scr=cv.imread('soccer.jpg')

b_plane, g_plane, r_plane = cv.split(scr)


_, t_130 = cv.threshold(r_plane, 130, 255, cv.THRESH_BINARY)        

t, t_otsu = cv.threshold(r_plane, -1, 255,  cv.THRESH_BINARY | cv.THRESH_OTSU) 

print('otsu threshold:', t)                 

imgs = {'Original': scr, 't:130':t_130, 'otsu:%d'%t: t_otsu}

#Task3_Otsu Binarization with Rose.jpg

grose=cv.imread('rose.png', cv.IMREAD_GRAYSCALE)
crose=cv.imread('rose.png')

b_plane, g_plane, r_plane = cv.split(crose)

b_plane = scr[:, :, 0]
g_plane = scr[:, :, 1]
r_plane = scr[:, :, 2]


'''
for i , (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='Paired')
    plt.xticks([]); plt.yticks([])
'''
plt.show()