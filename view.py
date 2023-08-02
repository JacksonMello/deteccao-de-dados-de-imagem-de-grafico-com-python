import cv2 as cv

img = cv.imread('tabela.png',cv.IMREAD_GRAYSCALE)
ret,thresh = cv.threshold(img,160,255,cv.THRESH_BINARY)
cv.imwrite('thresh_tabela.png',thresh)