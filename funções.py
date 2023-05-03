# trabalho ep2 Henrique Albuquerque e Rafael Rayes
# funções

# Exercicio 1: Define posição
# Henrique
def define_posicoes (linha, coluna, orientacao, tamanho):
    posicao = []
    if orientacao == 'vertical':
        for i in range (0, tamanho):
            linha_da_casa = linha + i 
            coluna_da_casa = coluna
            casa = [linha_da_casa, coluna_da_casa]
            posicao.append(casa)
    if orientacao == 'horizontal':
        for i in range (0, tamanho):
            linha_da_casa = linha
            coluna_da_casa = coluna + i
            casa = [linha_da_casa, coluna_da_casa]
            posicao.append(casa)
    return posicao
# Rafa
def define_posicoes(x, y, orietacao, tamanho):
    posicao = []
    for i in range(tamanho):
        if orietacao == "vertical":
            posicao.append([x+i,y])
        else:
            posicao.append([x,y+i])
    return posicao

# Exercicio 2: Preenche Frota
# Henrique
def preenche_frota (frota, navio, x, y, orientacao, tamanho):
    posicao = define_posicoes(x, y, orientacao, tamanho)
    if navio in frota:
        frota[navio].append(posicao)
    else:
        frota[navio] = [posicao]
    return frota
# Rafa

# Exercicio 3: Faz Jogada
# Henrique
def faz_jogada (tabuleiro, x, y):
    if tabuleiro[x][y] == 1:
        tabuleiro[x][y] = 'X'
    else:
        tabuleiro[x][y] = '-'
    return tabuleiro
# Rafa

# Exercicio 4: Posiciona Frota
# Henrique
def posiciona_frota (dic_info):
    tabuleiro = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]
    for tipo in dic_info:
        for frota in dic_info[tipo]:
            for cordenada in frota:
                tabuleiro[cordenada[0]][cordenada[1]] = 1
    return tabuleiro
# Rafa

# Exercicio 5: Quantas embarcações afundadas?
def afundados (frota, tabuleiro):
    afundados = 0
    for navio in frota:
        for unidade in frota[navio]:
            validacao = []
            for posicao in unidade:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    break
                if posicao == unidade[-1] and tabuleiro[posicao[0]][posicao[1]] == 'X':
                    afundados += 1
    return afundados