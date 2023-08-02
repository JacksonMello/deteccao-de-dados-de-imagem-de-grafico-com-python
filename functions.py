import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('thresh_tabela.png',0)

def get_pixeis():
    PONTOS = []
    for lin in range(img.shape[0]):
        for col in range(img.shape[1]):
            if img[lin,col] == 0:
                PONTOS.append([lin,col])
                
    return PONTOS

def get_origem(PONTOS):
    min = [500,500]
    max = [-1,-1]
    for ponto in PONTOS:
        if ponto[0] < min[0] and ponto[1] < min[1] : min = ponto
        if ponto[0] > min[0] and ponto[1] > min[1] : max = ponto

    # min: [5, 3] --> canto superior esquerdo
    # max: [300, 435] --> canto direito inferior
    #Origem do gráfico: [300, 3]
    
    ORIGEM = [max[0], min[1]]

    return [ORIGEM, min, max]

def get_cor(PONTO):
    print(img[PONTO[0],PONTO[1] + 1])
    
def get_componentes(PONTOS, ORIGEM):
    
    EIXO_X = []
    EIXO_Y = []
    CURVA = []
    
    #extrair eixos
    for ponto in PONTOS:
        if ponto[0] == ORIGEM[0]:   #eixo X
            EIXO_X.append(ponto)
        elif ponto[1] == ORIGEM[1]: #eixo Y
            EIXO_Y.append(ponto)
        else:                       #pontos da curva
            CURVA.append(ponto)
    
    return [EIXO_X, EIXO_Y, CURVA]

def refinar_curva(EIXO_X, CURVA):
    # print(f'Total de pontos na curva: {len(CURVA)}')
    # print(f'img.shape: {img.shape}')
    CURVA_REFINADA = []
    for x in EIXO_X:
        pontos_Y = []
        for ponto in CURVA:
            if x[1] == ponto[1]:
                pontos_Y.append(ponto)
                
        n = len(pontos_Y)
        if n == 0 : continue
        
        if n % 2 == 0: #número par de pontos
            CURVA_REFINADA.append(pontos_Y[int(n/2 - 1)])
        else:          #número ímpar de pontos
            CURVA_REFINADA.append(pontos_Y[int(n//2)])
    
    return CURVA_REFINADA

def get_tab_px(EIXO_X, CURVA_REFINADA):
    
    EIXO_X.pop(0) #extrai o ponto da origem (0, 0), pois a curva não possui correspondente para este pixel

    TAB_PIXEIS = []
    cont_px = 0
    for pixel in EIXO_X:
        
        y = pixel[0] - CURVA_REFINADA[cont_px][0]
        TAB_PIXEIS.append([cont_px + 1, y])

        cont_px += 1

    return TAB_PIXEIS

def get_tab_final(TABELA_PX, ORIGEM_REAL, RANGE_REAL, RANGE_PX):

    const_X = RANGE_REAL[0] / RANGE_PX[0] #o valor real de 1px em X
    const_Y = RANGE_REAL[1] / RANGE_PX[1] #o valor real de 1px em Y

    TAB_FINAL = []
    for ponto in TABELA_PX:

        X = ORIGEM_REAL[0] + const_X * ponto[0]
        Y = ORIGEM_REAL[1] + const_Y * ponto[1]
        TAB_FINAL.append([X,Y])
    
    return TAB_FINAL

def gerar_grafico(DADOS, ORIGEM_REAL, RANGE_REAL):
    
    EIXOS = [  # [xmin, xmax, ymin, ymax]
        ORIGEM_REAL[0],
        ORIGEM_REAL[0] + RANGE_REAL[0],
        ORIGEM_REAL[1],
        ORIGEM_REAL[1] + RANGE_REAL[1]
    ]
    LIST_X = []
    LIST_Y = []
    for coord in DADOS:
        LIST_X.append(coord[0])
        LIST_Y.append(coord[1])
    
    plt.plot(LIST_X, LIST_Y)
    plt.xlabel('Sut (MPa)')
    plt.ylabel('f')
    plt.axis(EIXOS)
    plt.show()