import cv2 as cv

img = cv.imread('thresh_tabela.png',0)
pontos = 0
for linha in range(img.shape[0]):
    for coluna in range(img.shape[1]):
        if img[linha,coluna] == 0:
            pontos += 1

print(f'Total de pixeis: {img.size}\nTotal de pontos: {pontos}')

#referência: canto superior esquerdo
#coluna 3
#linha 299