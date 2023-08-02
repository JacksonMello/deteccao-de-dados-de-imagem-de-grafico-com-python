from functions import *
import json

PIXEIS = get_pixeis()
REFS = get_origem(PIXEIS) #retorna coordenadas na img de ORIGEM, min e max, respectivamente.

[EIXO_X, EIXO_Y, CURVA] = get_componentes(PIXEIS, REFS[0]) #eixos X, eixo Y e a CURVA

# print(f'Eixo X: {len(EIXO_X)}')
# print(f'Eixo Y: {len(EIXO_Y)}')

CURVA_REFINADA = refinar_curva(EIXO_X, CURVA)
TAB_PIXEIS = get_tab_px(EIXO_X, CURVA_REFINADA)

h_0 = REFS[2][0] - REFS[1][0] #valor máximo na origem
TAB_PIXEIS.insert(0, [0,h_0])

ORIGEM_REAL = [490, 0.76]
RANGE_REAL = [910, 0.14]
RANGE_PX = [len(EIXO_X),len(EIXO_Y)] #acrecenta-se 1 ao eixo Y pois este pixel não foi incluido neste eixo na extração de componentes

TAB_FINAL = get_tab_final(TAB_PIXEIS, ORIGEM_REAL, RANGE_REAL, RANGE_PX)

# arquivo = open('Coord_Grafico_f.json', 'w')
# json.dump(TAB_FINAL,arquivo)
# arquivo.close()

gerar_grafico(TAB_FINAL, ORIGEM_REAL, RANGE_REAL)