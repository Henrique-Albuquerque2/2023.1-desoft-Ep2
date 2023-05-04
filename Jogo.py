
def define_posicoes(linha, coluna, orietacao, tamanho):
    posicao = []
    for i in range(tamanho):
        if orietacao == "vertical":
            posicao.append([linha+i,coluna])
        else:
            posicao.append([linha,coluna+i])
    return posicao
def preenche_frota(frota, navio, linha, coluna, orientacao, tamanho):
    posicao = define_posicoes(linha, coluna, orientacao, tamanho)
    if navio in frota:
        frota[navio].append(posicao)
    else:
        frota[navio] = [posicao]
    return frota
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(frota):
    tabuleiro = [[0 for _ in range(10)] for _ in range(10)]
    for posicoes in frota.values():
        for posicao in posicoes:
            for coordenada in posicao:
                linha, coluna = coordenada
                tabuleiro[linha][coluna] = 1
    return tabuleiro
def afundados(frota, tabuleiro):
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

navios = {
    "porta-aviões":[1, 4],
    "navio-tanque":[2, 3],
    "contratorpedeiro":[3, 2],
    "submarino": [4, 1],
}
frota = {}
for navio, specs in navios.items():
    posicionamentos = 0
    while posicionamentos != specs[0]:
        print("Insira as informações referentes ao navio {} que possui tamanho {}".format(navio, specs[1]))
        linha = int(input("Linha:"))
        coluna = int(input("Coluna:"))
        if navio != "submarino":
            orientacao = int(input("[1] Vertical [2] Horizontal >"))
            if orientacao-1:
                orientacao = "horizontal"
            elif not orientacao-1:
                orientacao = "vertical"
        if not posicao_valida(frota, linha, coluna, orientacao, specs[1]):
            print("Esta posição não está válida!")
        else:
            preenche_frota(frota, navio, linha, coluna, orientacao, specs[1])
            posicionamentos +=1

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
tabuleiroJogador = posiciona_frota(frota)
tabuleiroInimigo = posiciona_frota(frota_oponente)
def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
print(monta_tabuleiros(tabuleiroJogador, tabuleiroInimigo))
jogadas = []
while afundados(frota_oponente, tabuleiroInimigo) != 10:
    #ataque = input("Insira a coordenada de ataque: ").split('x')
    linha = int(input("Jogador, qual linha deseja atacar? "))
    coluna = int(input("Jogador, qual coluna deseja atacar? "))
    if linha>9 or coluna>9 or linha<0 or coluna<0:
        print("Coordenada inválida!")
        continue
    if [linha, coluna] in jogadas:
        print("A posição linha {} e coluna {} já foi informada anteriormente! ".format(linha, coluna))
        continue
    jogadas.append([linha, coluna])
    tabuleiroInimigo = faz_jogada(tabuleiroInimigo, linha, coluna)
    print(monta_tabuleiros(tabuleiroJogador, tabuleiroInimigo))
print("Parabéns! Você derrubou todos os navios do seu oponente!")