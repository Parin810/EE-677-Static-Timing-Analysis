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
                #print self.graph
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
                        #print "value of u =",s
                        #print "self graph no:",self.graph_no,self.graph[s]
                        for i in self.graph[s]:                               
                                if visited[i]==False:
                                        self.getAllPaths(i, d, visited, path)             
                path.pop()
                #print path
                visited[s]= False           
                return path_list
        def Paths(self,src, dest):           
                visited =[False]*(self.N)               
                path = []
                #print"original path",path
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
        def convert(self,vertex,path):
                #print path,vertex
                temp=[]
                for i in range (0,(len(path))):
                        u=path[i]
                        v=vertex[u]
                        temp.append(v)
                        #print "convert=",temp
                return temp
        
##########################################################
weight=0
All_weight=[]
nodes=[]
Edges = []
Path_Names=[]
#vertex = ['and1_A', 'and1_B', 'or1_A', 'or1_B', 'w1', 'w2', 'and1', 'w3', 'or1','sink_in']
vertex = ['amr','mum','pune','powai','andr','blr','delhi','kol']

for i in range (0,len(vertex)):
        nodes.append(i)
print "nodes",nodes
#Edges_in=[('and1_A', 'and1', 2), ('and1_B', 'and1', 2), ('or1_A', 'or1', 0), ('or1_B', 'or1', 0), ('w1', 'and1_A', 1), ('w2', 'and1_B', 2), ('and1', 'or1_A', 3), ('w3', 'or1_B', 4), ('or1', 'sink_in', 0)]
Edges_in=[('amr','mum',1),('amr','pune',2),('amr','kol',20),('mum','delhi',3),('andr','powai',10),('pune','andr',25),('powai','pune',7),('delhi','kol',15),('delhi','amr',100),('delhi','blr',6),('blr','mum',22),('kol','powai',9)]
print "edges_in",Edges_in
for i in range (0,len(Edges_in)):
        temp = []
        for j in range (0,3):
                if Edges_in[i][j] in vertex:
                        #print Edges_in[i][j]
                        a= vertex.index(Edges_in[i][j])
                        #print a
                        #temp=vertex.index(Edges[i][j])
                else:
                        a = Edges_in[i][j]

                temp.append(a)
        #print "temp",temp
        Edges.append(tuple(temp))
print "Edges =",Edges
#nodes=[0,1,2,3,4,5,6]
#Edges=[(0,1,1),(0,2,4),(0,3,10),(1,4,2),(2,3,1),(3,5,2),(3,1,5),(3,4,10),(4,5,6),(4,6,3),(5,6,3),(6,0,8),(6,2,9)]

g = Graph(len(nodes))
Edge=len(Edges)

Source='amr'
Destination='powai'

src =vertex.index(Source)
dest=vertex.index(Destination)
print "Given parameters"
print "Nodes =",nodes
print "Edges =",Edges
print "Process Started..."
print "Total nodes =",len(nodes),"and Total Edges =",Edge
for i in range (0,Edge):
      #  print(E[i][0]),(E[i][1])
        g.addEdge(Edges[i][0],Edges[i][1])
print "###########################################################"
path=g.Paths(src, dest)
print "Calculating................"
print "###########################################################"
print "Process complated."
print "All possible path from",Source,"to",Destination,"are",len(path)
#print "Total no of path found",len(path)

for i in range (0,len(path)):
        if len(path)==0:
                print "No path found"              
        else:
               #print "Path no %d ="%(i+1), path[i]
               # print Edges[0][0],path[0][0]               
                weight=g.calc_weight(Edges,path[i])
                All_weight.append(weight)
                path_name=g.convert(vertex,path[i])
                print "Path no %d ="%(i+1), path_name,".....has Weight =",weight
                #print "Path no %d ="%(i+1), path[i],".....has Weight =",weight
        Path_Names.append(path_name)
        
#print "All Paths are=",Path_Names
print "All_Path_weight =",All_weight




                
        
