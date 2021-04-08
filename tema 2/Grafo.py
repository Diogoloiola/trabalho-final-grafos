def twoColorUtil(G, src, N, colorArr):  
      
    colorArr[src] = 1 
      
    q = [src] 
      
    while len(q) > 0: 
          
        u = q.pop(0) 
          
        for v in range(0, len(G[u])): 
      

            if colorArr[G[u][v]] == -1: 
              
        
                colorArr[G[u][v]] = 1 - colorArr[u] 
                q.append(G[u][v]) 
               
           
            elif colorArr[G[u][v]] == colorArr[u]:         
                return False 
          
    return True 
       
def twoColor(G, N):  
    colorArr = [0] * (N + 1)
    for i in range(1, N + 1):
        colorArr[i] = -1
       
    for i in range(1, N): 
        if colorArr[i] == -1: 
            if twoColorUtil(G, i, N, colorArr) == False: 
                return False 
              
            return True 
   
def isOddSum(info, n, m): 
      
    G = [[] for i in range(2*n)] 
      
    pseudo, pseudo_count = n+1, 0 
    for i in range(0, m): 
          
        if info[i][2] % 2 == 1: 
              
            u, v = info[i][0], info[i][1] 
            G[u].append(v) 
            G[v].append(u) 
           
        else: 
            u, v = info[i][0], info[i][1] 
  
            G[u].append(pseudo) 
            G[pseudo].append(u) 
            G[v].append(pseudo) 
            G[pseudo].append(v) 
              
            pseudo_count += 1
  
           
            pseudo += 1 
     
    return twoColor(G, n+pseudo_count) 
