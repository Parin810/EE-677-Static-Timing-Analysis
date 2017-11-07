import networkx as ng

class Graph:
    
    def __init__(self,vertices=0,default_dict=None):
        self.vertices = vertices
        if default_dict==None:
            self.graph=dict()
            self.graph={}
    def add_vertex(self,vertex):
        if vertex not in self.graph.keys():
            self.graph[vertex]=[[None],[None]]
            self.vertices=self.vertices+1
            
    def add_edge(self,edgeset=[]):
        """edgeset = [u,v,weight]"""
        self.edgeset=list(edgeset)
  
        self.fanout=self.edgeset[1]
        self.fanin=self.edgeset[0]
        
        print self.fanin,self.fanout
        
        if self.graph[self.edgeset[0]][0]==[None]:
            self.graph[self.edgeset[0]][0].remove(None)
        
        self.graph[self.edgeset[0]][0].append(self.fanout)
        
        if self.graph[self.edgeset[1]][1]==[None]:
            self.graph[self.edgeset[1]][1].remove(None)
        
        if self.fanin not in self.graph[self.fanin][1]:
            self.graph[self.edgeset[1]][1].append(self.fanin)
    
        
    def num_vertices(self):
        return len(self.graph.keys())
    
    def get_vertices(self):
        return self.graph.keys()
    
    def get_in_degrees(self):
        self.in_degrees = []
        for i in sorted(self.graph.keys()):
            self.in_degrees.append(len(self.graph[i][1]))
        return self.in_degrees
g1=Graph(2)

print g1.vertices

for i in range(1,6):
    g1.add_vertex(i)
    
g1.add_edge([1,3])
g1.add_edge([2,3])
g1.add_edge([3,4])
g1.add_edge([3,5])
g1.add_edge([4,5])

print g1.graph
print g1.num_vertices()
print g1.get_vertices()
print g1.get_in_degrees()

