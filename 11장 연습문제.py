#P11.1
graphAL ={'A' : set([('B',29),('F',10)          ]),
        'B' : set([('A',29),('C',16), ('G',15)]),
        'C' : set([('B',16),('D',12)          ]),
        'D' : set([('C',12),('E',22), ('G',18)]),
        'E' : set([('D',22),('F',27), ('G',25)]),
        'F' : set([('A',10),('E',27)          ]),
        'G' : set([('B',15),('D',18), ('E',25)]) }

def printAllEdges(graph):
    plist = []		
    for v in graph:  
        plist.append(v)           
        for e in graph[v]:
            if e[0] not in plist:      
                print("(%s,%s,%d)"%(v,e[0],e[1]), end=' ')

printAllEdges(graphAL)

#P11.2, 11.3
import heapq
parent = []     				
set_size = 0    				

def init_set(nSets) :			
    global set_size, parent 	
    set_size = nSets;			
    for i in range(nSets):		
        parent.append(-1)		

def find(id) :					
    while (parent[id] >= 0) :	
        id = parent[id]			
    return id;					

def union(s1, s2) :				
    global set_size				
    parent[s1] = s2				
    set_size = set_size - 1		

def MSTKruskal(vertex, adj):		
    vsize = len(vertex)             
    init_set(vsize)                 
    eList = []
    test = []
    sum = 0                      

    for i in range(vsize-1) :       
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                eList.append( adj[i][j] )

    heapq.heapify(eList)

    for i in range(0, len(eList)):
        n = heapq.heappop(eList)
        test.append(n)

    eList[:] = test[:]

    for i in range(vsize-1) :       
        for j in range(i+1, vsize) :
            for k in range(len(eList)):
                if eList[k] == adj[i][j]:
                    eList[k] = (i,j,adj[i][j])
     
    edgeAccepted = 0
    while (edgeAccepted < vsize - 1) :	
        e = eList.pop(0)       		
        uset = find(e[0])      			
        vset = find(e[1])

        if uset != vset :       		
            print("간선 추가 : (%s, %s, %d)" %
				(vertex[e[0]], vertex[e[1]], e[2]))
            sum += e[2]
            union(uset, vset)   	
            edgeAccepted += 1 
    print(sum)

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]    

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)

#P11.5
parent = []     				
set_size = 0    				

def init_set(nSets) :			
    global set_size, parent 	
    set_size = nSets;			
    for i in range(nSets):		
        parent.append(-1)		

def find(id) :					
    while (parent[id] >= 0) :	
        id = parent[id]			
    return id;					

def union(s1, s2) :				
    global set_size				
    parent[s1] = s2				
    set_size = set_size - 1		

def MSTKruskal(vertex, adj):		
    vsize = len(vertex)             
    init_set(vsize)                 
    eList = []                      

    for i in range(vsize-1) :       
        for j in range(i+1, vsize) :
            if adj[i][j] != None :
                eList.append( (i,j,adj[i][j]) )

    eList.sort(key= lambda e : e[2], reverse=False)

    edgeAccepted = 0
    while (edgeAccepted < vsize - 1) :	
        e = eList.pop(-1)       		
        uset = find(e[0])      			
        vset = find(e[1])

        if uset != vset :       		
            print("간선 추가 : (%s, %s, %d)" %
				(vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)   	
            edgeAccepted += 1   	

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]    

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex, weight)

#P11.6
INF = 9999
def choose_vertex(dist, found) :			
    min = INF
    minpos = -1
    for i in range(len(dist)) :				
        if dist[i]<min and found[i]==False:	
            min = dist[i]
            minpos = i
    return minpos;							

def shortest_path_dijkstra(vtx, adj, start) :
    vsize = len(vtx)						
    dist = list(adj[start])					
    path = [start] * vsize					
    found= [False] * vsize					
    found[start] = True						
    dist[start] = 0							

    for i in range(vsize) :
        print("Step%2d: "%(i+1), dist)  	
        u = choose_vertex(dist, found)		
        found[u] = True						

        for w in range(vsize) :				
            if not found[w] :				
                if dist[u] + adj[u][w] < dist[w] :	
                    dist[w] = dist[u] + adj[u][w]	
                    path[w] = u						

    return path							            

vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [0,	    7,		INF,	INF,	3,      10,		INF	],
           [7,		0,	    4,		10,	    2,	    6,	    INF	],
           [INF,	4,		0,		2,		INF,	INF,	INF	],
           [INF,	10,		2,		0,      11,		9,		4   ],
           [3,	    2,	    INF,   	11,		0,      13,		5   ],
           [10,	6,	    INF,		9,      13,		0,		INF	],
           [INF,   INF,		INF,   	4,		5,		INF,	0   ] ]    

print("Shortest Path By Dijkstra Algorithm")
start = 0		
path = shortest_path_dijkstra(vertex, weight, start)

for end in range(len(vertex)) :
    dist = 0
    if end != start :
        print("[최단경로: %s->%s] %s" %
				(vertex[start], vertex[end], vertex[end]), end='')
        while (path[end] != start) :
            dist = dist + weight[end][path[end]]
            print(" <- %s" % vertex[path[end]], end='')
            end = path[end]
        print(" <- %s" % vertex[path[end]])
        dist = dist + weight[end][path[end]]
        print(dist)
