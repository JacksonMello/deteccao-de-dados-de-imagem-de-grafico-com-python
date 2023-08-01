from functions import get_pixeis, get_origem, get_componentes, refinar_curva

PIXEIS = get_pixeis()
REFS = get_origem(PIXEIS)

[EIXO_X, EIXO_Y, CURVA] = get_componentes(PIXEIS, REFS[0]) #eixos X, eixo Y e a CURVA

print(f'Eixo X: {len(EIXO_X)}')
print(f'Eixo Y: {len(EIXO_Y)}')

CURVA_REFINADA = refinar_curva(EIXO_X, CURVA)
print(f'Total de pontos Final: {len(CURVA_REFINADA)}')
