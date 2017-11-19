from collections import defaultdict
global path_list
path_list=[]
#global path_no
#path_no=0
class Graph:
        def __init__(self,nodes):
                self.V= nodes
                self.graph = defaultdict(list)
                self.path_no=0                
                global path_list
                #global path_no
        def addEdge(self,u,v):
                self.graph[u].append(v)
        def printAllPathsUtil(self, u, d, visited, path):               
                visited[u]= True
                path.append(u)
                
                if u ==d:
                        #self.path_no +=1
                        #print "Path No =",self.path_no, path
                        path_list.append(path[:])
                        lenghtA=len(path) 
                        #print lenghtA, u,d,visited
                else:
                        for i in self.graph[u]:                               
                                if visited[i]==False:
                                        self.printAllPathsUtil(i, d, visited, path)             
                path.pop()
                visited[u]= False
                return path_list
        def AllPaths(self,src, dest):           
                visited =[False]*(self.V)               
                path = []
                path = self.printAllPathsUtil(src, dest,visited, path)
                return path
        
##########################################################
        
nodes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
Edges=[(0,1),(0,4),(1,8),(2,8),(4,5),(4,2),(5,9),(6,11),(7,6),(7,0),(8,12),(9,7),(10,3),(10,7),(11,13),(12,10),(13,10)]

g = Graph(len(nodes))
Edge=len(Edges)

src = 11
dest = 1
print "Total nodes =",len(nodes),"and Total Edges =",Edge
for i in range (0,Edge):
      #  print(E[i][0]),(E[i][1])
        g.addEdge(Edges[i][0],Edges[i][1])
path=g.AllPaths(src, dest)
print "All possible path from %d to %d are:"%(src, dest),len(path)
#print "Total no of path found",len(path)
for i in range (0,len(path)):
        if len(path)==0:
                print "No path found"               
        else:
                print "Path no %d ="%(i+1), path[i]

