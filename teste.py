def define_posicoes(x, y, orietacao, tamanho):
    lista = []
    for i in range(tamanho):
        if orietacao == "vertical":
            lista.append([x+i,y])
        else:
            lista.append([x,y+i])
    return lista