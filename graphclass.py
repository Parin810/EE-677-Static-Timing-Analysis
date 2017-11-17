import networkx as ng
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import write_dot


import networkx as ng
import matplotlib.pyplot as plt

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
        #print self.edgeset[0]
        self.fanout=self.edgeset[1]
        self.fanin=self.edgeset[0]
        
        print self.fanin,self.fanout
        
        
        if len(self.edgeset)==3:
            self.graph[self.edgeset[0]].append(self.edgeset[2])
        
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
    
    
    def get_weight(self,u,v):
        """Returns the edge weight from u to v"""
        if u not in self.graph.keys():
            return None
        if v not in self.graph.keys():
            return None
        try:
            index = self.graph[u][0].index(v)
            return (self.graph[u][index+2])
        except:
            return None
        
    
    def draw(self):
        dg=ng.DiGraph()
        #self.pair=[]
        #self.edgepair=[]
        for i in self.graph.keys():
            pair =self.graph[i][0]
            #print pair
            if pair!=[None]:
                for k in range(0,len(pair)):
                    dg.add_edge(i,pair[k])
                
        ng.draw(dg,with_labels=True,edge_labels=True,arrows=True)
        plt.show()

##toposort#
if __name__== '__main__':
    
  g1=Graph(2)

  print g1.vertices

  for i in range(1,6):
      g1.add_vertex(i)
      
  g1.add_edge([1,2])
  g1.add_edge([3,2])
  g1.add_edge([4,2])
  g1.add_edge([4,5])
  g1.add_edge([2,5])
  g1.draw()



  dynamic_in_degrees=[]
  dynamic_in_degrees=g1.get_in_degrees()

  print dynamic_in_degrees

  nextup=[]
  next_up=[i for i in range(0,len(dynamic_in_degrees)) if dynamic_in_degrees[i]==0]

  print next_up
                            
  out_order=[]
  out=[]

  while (len(next_up)!=0):
      out_order.append(next_up[0]+1)
      out=g1.get_outneigbours(next_up[0]+1)
      if out==[None]:
          break
      print "out",out
      del(next_up[0])
      print "next_up",next_up
      for i in out:
          dynamic_in_degrees[i-1]=dynamic_in_degrees[i-1]-1
          #print "dynamic_in_degrees", dynamic_in_degrees
          if dynamic_in_degrees[i-1]==0:
              next_up.append(i-1)
              print next_up
      
  print out_order

      



    
