'''
Author: Saurav Shandilya, Parin Chheda, Piyush Manavar
Date: 06/07/2017
Credits: EE-677 source material, Ch-1.13.2. Inheritance: Logic Gates and Circuits on http://interactivepython.org and http://www.geeksforgeeks.org

Name: Implementation of basic Logic gates, source, sink and connectors

Description: 
- Input to logic gate is provided using source block. One source block per input.
- Source is connected to gate using connectors
- Output of logic gate is taken at sink block via connector. One putput per source block.

'''



from collections import defaultdict
global path_list
path_list=[]
#global path_no
#path_no=0
class Graph:
        def __init__(self,nodes):
                self.N= nodes
                self.graph = defaultdict(list)
                self.path_no=0
                self.graph_no=0
                global path_list
                #global path_no
        def addEdge(self,s,v):
                self.graph[s].append(v)
                print self.graph
        def getAllPaths(self, s, d, visited, path):               
                visited[s]= True
                path.append(s)                
                if s == d:
                        #self.path_no +=1
                        #print "Path No =",self.path_no, path
                        path_list.append(path[:])
                        lenghtA=len(path) 
                        #print lenghtA, s,d,visited
                else:
                        self.graph_no +=1
                        print "value of u =",s
                        print "self graph no:",self.graph_no,self.graph[s]
                        for i in self.graph[s]:                               
                                if visited[i]==False:
                                        self.getAllPaths(i, d, visited, path)             
                path.pop()
                print path
                visited[s]= False           
                return path_list
        def Paths(self,src, dest):           
                visited =[False]*(self.N)               
                path = []
                print"original path",path
                path = self.getAllPaths(src, dest,visited, path)
                return path
        
##########################################################
        
nodes=[0,1,2,3,4,5,6,7,8,9,10,11,12,13]
Edges=[(0,1),(0,4),(1,8),(1,6),(2,8),(4,5),(4,2),(5,9),(5,3),(6,11),(7,6),(7,0),(7,8),(8,6),(8,12),(9,7),(10,3),(10,7),(11,9),(11,5),(11,13),(12,10),(13,10)]

g = Graph(len(nodes))
Edge=len(Edges)

src =0
dest=3
print "Total nodes =",len(nodes),"and Total Edges =",Edge
for i in range (0,Edge):
      #  print(E[i][0]),(E[i][1])
        g.addEdge(Edges[i][0],Edges[i][1])
print "###########################################################"

print "###########################################################"

path=g.Paths(src, dest)

print "###########################################################"
print "All possible path from %d to %d are:"%(src, dest),len(path)
#print "Total no of path found",len(path)
for i in range (0,len(path)):
        if len(path)==0:
                print "No path found"               
        else:
                print "Path no %d ="%(i+1), path[i]

