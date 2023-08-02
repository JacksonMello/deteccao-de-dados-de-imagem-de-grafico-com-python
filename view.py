import cv2 as cv

#gerar gráfico em escala de cinza e nesta selecionar apenas os píxeis com intencidade até 160, os demais pixeis serão 255 (branco).

img = cv.imread('tabela.png',cv.IMREAD_GRAYSCALE)
ret,thresh = cv.threshold(img,160,255,cv.THRESH_BINARY)
cv.imwrite('thresh_tabela.png',thresh) #Salvar imagem para coleta de pixeis
