import networkx as ng

class Graph:
    """Graph data structure : dict={node : [out],[in],attribute}"""
    def __init__(self,vertices=0,default_dict=None):
        self.vertices = vertices
        if default_dict==None:
            self.graph=dict()
            self.graph={}
    def add_vertex(self,vertex):
    """Adds vertex to graph dict if not added"""
        if vertex not in self.graph.keys():
            self.graph[vertex]=[[None],[None]]
            self.vertices=self.vertices+1
            
    def add_edge(self,edgeset=[]):
        """edgeset = [u,v,weight], populates in and out accordingly"""
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
        """Returns number of vertices"""
        return len(self.graph.keys())
    
    def get_vertices(self):
        """returns a list of vertices"""
        return self.graph.keys()
    
    def get_in_degrees(self):
        """Returns a vertex indexed list of in_degrees"""
        self.in_degrees = []
        for i in sorted(self.graph.keys()):
            if any(self.graph[i][1])==True:
                self.in_degrees.append(len(self.graph[i][1]))
            else:
                self.in_degrees.append(0)
        return self.in_degrees
    
    def get_outneigbours(self,vertex):
        """Returns a list containing out neigbours of a vertex"""
        if vertex not in (self.graph.keys()):
            return None
        else:
            return (self.graph[vertex][0])
     
    def get_inneigbours(self,vertex):
        """Returns a list containing in neigbours of a vertex"""
        if vertex not in (self.graph.keys()):
            return None
        else:
            return (self.graph[vertex][1])
    
    
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
print g1.get_outneigbours(3)

