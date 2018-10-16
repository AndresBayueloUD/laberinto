def txtToArray(txt):
    if isinstance(txt, str):
        return txtToArray(txt.split("\n"))
    if isinstance(txt, list):
        if len(txt) > 1:
            return [list(map(int, txt[0].split(" ")))] + txtToArray(txt[1:])
        else:
            return [list(map(int, txt[0].split(" ")))]

def camino(matriz, crdn_start, crdn_end, previus_crdn = []):
    if matriz[crdn_start[0]][crdn_start[1]] == 1:
        return False
    if matriz[crdn_start[0]][crdn_start[1]] == 0:
        if crdn_start[0] == crdn_end[0] and crdn_start[1] == crdn_end[1]:
            return True
        else:
            return psblCamino(matriz, crdn_start, [crdn_start[0]+1, crdn_start[1]], crdn_end, previus_crdn) or psblCamino(matriz, crdn_start, [crdn_start[0], crdn_start[1]+1], crdn_end, previus_crdn) or psblCamino(matriz, crdn_start, [crdn_start[0]-1, crdn_start[1]], crdn_end, previus_crdn) or psblCamino(matriz, crdn_start, [crdn_start[0], crdn_start[1]-1], crdn_end, previus_crdn)

def psblCamino(matriz, crdn_start, next_crdn, crdn_end, previus_crdn):
    if comprobarCamino(previus_crdn, next_crdn):
        return False
    else:
        return camino(matriz, next_crdn, crdn_end, previus_crdn + [crdn_start])

def comprobarCamino(camino, crdn):
    if(len(camino)>0):
        if camino[0] == crdn:
            return True
        else:
            return comprobarCamino(camino[1:len(camino)], crdn)
    else:
        return False

'''def psblCamino(matriz, crdn_start, next_crdn, crdn_end, previus_crdn):
    if next_crdn == previus_crdn:
        return False
    else:
        return camino(matriz, next_crdn, crdn_end, crdn_start)'''
