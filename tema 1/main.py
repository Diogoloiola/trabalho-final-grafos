from os import error
import sys
import Graph
if __name__ == "__main__":
    try:
        if len(sys.argv) == 1:
           raise error('arquivo de entrada nao fornecido')
        else:
            f = open(sys.argv[1],'r')
            u, v = f.readline().split(' ')
            u = int(u)
            v = int(v)
            matriz = []
            for j in range(0, u):
                edge = f.readline().replace("\n","").split(" ")
                matriz.append(list(map(int, edge)))
            a = Graph.Grafo(u)
            a.grafo = matriz
            if a.eBipartido():
                print('possui ciclos pares')
            else:
                print('nao possui ciclos pares')
    except:
        raise error('erro ao abrir o arquivo')