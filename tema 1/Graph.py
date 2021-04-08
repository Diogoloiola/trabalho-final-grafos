class Grafo():
 
    def __init__(self, V):
        self.V = V
        self.grafo = [[0 for column in range(V)]
                      for row in range(V)]
 
        self.coresVetor = [-1 for i in range(self.V)]
 
   
    def funcAux(self, src):

        queue = []
        queue.append(src)
 

        while queue:
 
            u = queue.pop()
 
          
            if self.grafo[u][u] == 1:
                return False
 
            for v in range(self.V):
 
                if (self.grafo[u][v] == 1 and
                        self.coresVetor[v] == -1):

                    self.coresVetor[v] = 1 - self.coresVetor[u]
                    queue.append(v)
 
                elif (self.grafo[u][v] == 1 and
                      self.coresVetor[v] == self.coresVetor[u]):
                    return False
        return True
 
    def eBipartido(self):
        self.coresVetor = [-1 for i in range(self.V)]
        for i in range(self.V):
            if self.coresVetor[i] == -1:
                if not self.funcAux(i):
                    return False
        return True
 