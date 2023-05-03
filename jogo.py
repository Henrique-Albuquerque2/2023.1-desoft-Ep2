# trabalho ep2 Henrique Albuquerque e Rafael Rayes
print ('hello world')

def afundados (frota, tabuleiro):
    afundados = 0
    for navio in frota:
        for unidade in navio:
            for posicao in unidade:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    break
                else:
                    afundados += 1
    return afundados

print(frota = { 
    "porta-aviões":[
      [[1,5],[1,6],[1,7],[1,8]]
    ],
    "navio-tanque":[
      [[6,1],[6,2],[6,3]],
      [[4,7],[5,7],[6,7]]
    ],
    "contratorpedeiro":[
      [[1,1],[2,1]],
      [[2,3],[3,3]],
      [[9,1],[9,2]]
    ],
    "submarino": [
      [[0,3]],
      [[4,5]],
      [[8,9]],
      [[8,4]]
    ],
}, tabuleiro = [
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 0, 0, 'X', 'X', 'X', 'X', 0],
  [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
])