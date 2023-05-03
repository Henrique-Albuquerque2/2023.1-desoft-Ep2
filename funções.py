# trabalho ep2 Henrique Albuquerque e Rafael Rayes
# funções

# Exercicio 1: Define posição
def define_posicoes(linha, coluna, orietacao, tamanho):
    posicao = []
    for i in range(tamanho):
        if orietacao == "vertical":
            posicao.append([linha+i,coluna])
        else:
            posicao.append([linha,coluna+i])
    return posicao

# Exercicio 2: Preenche Frota
def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if navio in frota:
        frota[navio].append(posicao)
    else:
        frota[navio] = [posicao]
    return frota

# Exercicio 3: Faz Jogada
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'linha'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
# Exercicio 4: Posiciona Frota
def posiciona_frota(frota):
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
    for posicoes in frota.values():
        for posicao in posicoes:
            for coordenada in posicao:
                linha, coluna = coordenada
                tabuleiro[linha][coluna] = 1
    return tabuleiro
# Exercicio 5: Quantas embarcações afundadas?
def afundados(frota, tabuleiro):
    afundados = 0
    for navio in frota:
        for unidade in frota[navio]:
            validacao = []
            for posicao in unidade:
                if tabuleiro[posicao[0]][posicao[1]] != 'linha':
                    break
                if posicao == unidade[-1] and tabuleiro[posicao[0]][posicao[1]] == 'linha':
                    afundados += 1
    return afundados

# Exercicio 6: Posição Válida
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    lista = define_posicoes(linha, coluna, orientacao, tamanho)
    if lista[0][0] < 0 or lista[0][1] < 0 or lista[-1][0] > 9 or lista[-1][1] >9:
        return False
    for i in lista:
        for navios in frota.values():
            for navio in navios:
                if i in navio:
                    return False
    return True
print("9x0".split('x'))