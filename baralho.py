def cria():
    naipes = ['C', 'E', 'O', 'P']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append((naipe, valor))
    return baralho

def calcula_ganhador(baralho_j1, baralho_j2):
    if len(baralho_j1) == 0 and len(baralho_j2) != 0:
        return 1
    elif len(baralho_j1) != 0 and len(baralho_j2) == 0:
        return 2
    else:
        return None
