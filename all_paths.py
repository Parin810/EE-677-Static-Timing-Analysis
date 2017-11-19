'''
Author: Saurav Shandilya, Parin Chheda, Piyush Manavar
Date: 19/11/2017
Credits: EE-677 source material, Ch-1.13.2. Inheritance: Logic Gates and Circuits on http://interactivepython.org and http://www.geeksforgeeks.org

Name: Implementation of finding all possible path in ginven graph

Description: 
- Input will takes Nodes, and edged 
- Source is the node from where the serch should start
- Destination is the node where search will end
- This code gives all the possible pathe in given DAG graph from source to destination  

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
        def getweight(self,A,B,Edges):
                for z in range (0,len(Edges)):
                        if A==Edges[z][0]:
                                if B==Edges[z][1]:
                                        return Edges[z][2]
        def calc_weight(self,Edges,path):
                #print "CalC Edges",Edges
                #print "Paths", path
                temp=0
                temp2=0
                for a in range (0,(len(path))-1):
                        temp=self.getweight(path[a],path[a+1],Edges)
                        temp2 = temp2+temp
                        #print "Temp2=",temp2
                return temp2
                        
        
##########################################################
weight=0       
nodes=[0,1,2,3,4]
Edges=[(0,1,1),(0,3,3),(1,2,4),(1,4,2),(2,3,5),(3,0,7),(4,3,6)]

g = Graph(len(nodes))
Edge=len(Edges)

src =2
dest=4
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
               # print Edges[0][0],path[0][0]
                weight=g.calc_weight(Edges,path[i])
                print "Weight for path %d="%(i+1),weight
                
                                
                                        
                    
                   
                                                
                                        
                                       
                                
                                
              



