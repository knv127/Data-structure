vertex = ['A','B','C','D','E','F','G','H']
adjMat = [[0,1,1,0,0,0,0,0],
        [1,0,0,1,0,0,0,0],
        [1,0,0,1,1,0,0,0],
        [0,1,1,0,0,1,0,0],
        [0,0,1,0,0,0,1,1],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,0,1,0]]

vlist = []
#P10.1
def dfs(start, adjMat):
    if vertex[start] not in vlist :			
        vlist.append(vertex[start])				
        print(vertex[start], end=' ')
        nbr = []
        for i in range(len(vertex)):
            if adjMat[start][i] > 0:
                nbr.append(i)
        for j in nbr:
            if vertex[j] in vlist:
                nbr.remove(j)				
        for v in nbr:					
            dfs(v, adjMat)

dfs(0, adjMat)

vlist2 = []
#P10.4
def dfsST(start, adjMat):
    if vertex[start] not in vlist2 :			
        vlist2.append(vertex[start])				
        nbr = []
        for i in range(len(vertex)):
            if adjMat[start][i] > 0:
                nbr.append(i)
        for j in nbr:
            if vertex[j] in vlist2:
                nbr.remove(j)				
        for v in nbr:
            if vertex[start] in vlist2 and vertex[v] not in vlist2:
                print("(",vertex[start],",",vertex[v],")", end=' ')					
            dfsST(v, adjMat)
            

dfsST(0, adjMat)

