from os import error
import sys

import Grafo

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise error('arquivo nao fornecido')
        exit()
    try:
        f = open(sys.argv[1],'r')
    except:
        raise error('erro ao abrir o arquivo')
    u, v = f.readline().replace('\n','').split(' ')
    n = int(u)
    m = int(v)
    matriz = []
    for j in range(0, n):
        edge = f.readline().replace("\n","").split(" ")
        if edge[0] != '':
            matriz.append(list(map(int, edge)))

    if not Grafo.isOddSum(matriz, n, m) == True: 
        print("No") 
    else:
        print("Yes")