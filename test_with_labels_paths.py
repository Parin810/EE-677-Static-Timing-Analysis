import networkx as ng
import matplotlib.pyplot as plt

class Graph:
    """Graph data structure : dict={node : [out],[in],attribute}"""
    def __init__(self,vertices=0,default_dict=None):
        self.vertices = vertices
        if default_dict==None:
            self.graph=dict()
            self.graph={}
    def add_vertex(self,vertex,label=''):
        """Adds vertex to graph dict if not added"""
        if vertex not in self.graph.keys():
            self.graph[vertex]=[label,[None],[None]]
            self.vertices=self.vertices+1
            
    def add_edge(self,edgeset=[]):
        """edgeset = [u,v,weight], populates in and out accordingly"""
        self.edgeset=list(edgeset)
        #print self.edgeset[0]
        self.fanout=self.edgeset[1]
        self.fanin=self.edgeset[0]
        
        #print self.fanin,self.fanout
        
        
        if len(self.edgeset)==3:
            self.graph[self.edgeset[0]].append(self.edgeset[2])
        
        if self.graph[self.edgeset[0]][1]==[None]:
            self.graph[self.edgeset[0]][1].remove(None)
        self.graph[self.edgeset[0]][1].append(self.fanout)
        
        if self.graph[self.edgeset[1]][2]==[None]:
            self.graph[self.edgeset[1]][2].remove(None)
        
        if self.fanin not in self.graph[self.fanin][2]:
            self.graph[self.edgeset[1]][2].append(self.fanin)
    
        
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
            if any(self.graph[i][2])==True:
                self.in_degrees.append(len(self.graph[i][2]))
            else:
                self.in_degrees.append(0)
        return self.in_degrees
    
    def get_outneigbours(self,vertex):
        """Returns a list containing out neigbours of a vertex"""
        if vertex not in (self.graph.keys()):
            return None
        else:
            return (self.graph[vertex][1])
     
    def get_inneigbours(self,vertex):
        """Returns a list containing in neigbours of a vertex"""
        if vertex not in (self.graph.keys()):
            return None
        else:
            return (self.graph[vertex][2])
    
    
    def get_weight(self,u,v):
        """Returns the edge weight from u to v"""
        if u not in self.graph.keys():
            return None
        if v not in self.graph.keys():
            return None
        try:
            index = self.graph[u][1].index(v)
            return (self.graph[u][index+3])
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
def toposort(g1):
	dynamic_in_degrees=[]
	dynamic_in_degrees=g1.get_in_degrees()
	nextup=[]
	next_up=[i for i in range(0,len(dynamic_in_degrees)) if dynamic_in_degrees[i]==0]
	out_order=[]
	out=[]
	while (len(next_up)!=0):
			out_order.append(next_up[0]+1)
			out=g1.get_outneigbours(next_up[0]+1)
			if out==[None]:
					break
			#print "out",out
			del(next_up[0])
			#print "next_up",next_up
			for i in out:
					dynamic_in_degrees[i-1]=dynamic_in_degrees[i-1]-1
					#print "dynamic_in_degrees", dynamic_in_degrees
					if dynamic_in_degrees[i-1]==0:
							next_up.append(i-1)
							#print next_up

	return out_order


def generate_ats(g1,toposort_list):
    nodes = toposort_list
    #print nodes
    ats = [0]*g1.num_vertices()

    for i in range(0,len(nodes)):
        fanin=g1.get_inneigbours(nodes[i])
        mat =0
        if any(fanin)==False:
            ats[nodes[i]-1]=0
            g1.graph[nodes[i]].append(mat)
            continue
        for k in fanin:
            #print "w",g1.get_weight(k,nodes[i])
            mat = max(mat, ats[k-1]+g1.get_weight(k,nodes[i]))  
        ats[nodes[i]-1]=mat
        g1.graph[nodes[i]].append(mat)
    return ats


def generate_rats_slack(g1,reverse_toposort_list,cycle_time=0):
    nodes = reverse_toposort_list
    #set max values for all rats
    rats = [100]*g1.num_vertices()
    for i in range(0,len(nodes)):
        fanout=g1.get_outneigbours(nodes[i])
        rat = 100
        #if no fanout, rat= cycle time
        if any(fanout)==False:
            #print nodes[i]
            rats[nodes[i]-1]=cycle_time
            #print nodes[i]-1,rats[nodes[i]-1]
            #print rats
            g1.graph[nodes[i]].append(cycle_time)
            slack = g1.graph[nodes[i]][-1] - g1.graph[nodes[i]][-2]
            g1.graph[nodes[i]].append(round(slack,2))
            continue
        for k in fanout:
            rat = min(rat,rats[k-1] - g1.get_weight(nodes[i],k))
        rats[nodes[i]-1] = round(rat,2)
        g1.graph[nodes[i]].append(rats[nodes[i]-1])
        #compute slack = rat - at at each node 
        slack = g1.graph[nodes[i]][-1] - g1.graph[nodes[i]][-2]
        g1.graph[nodes[i]].append(round(slack,2))
        
    return rats

    
def report_ats_rats_slack(g1):
    for node in g1.get_vertices():
        print "node:", g1.graph[node][0], ", AAT:", g1.graph[node][-3], ", RAT :" , g1.graph[node][-2], ", slack:", g1.graph[node][-1]
        print "\n"
 
 
def report_paths(g1, path, paths = []):
    vertex = path[-1]
    if vertex == 12:
        vertex=1
    if vertex in g1.get_vertices():
         for out_nodes in g1.get_outneigbours(vertex):
                new_path = path + [out_nodes]
                paths = report_paths(g1, new_path, paths)
    else:
         paths += [path]
    return paths
    

g1=Graph(2)
#using edge generated by Saurav

edge=[('source','w1',0),('source','w2',0),('source','w3',0),('and1_A', 'and1', 2), ('and1_B', 'and1', 2), 
      ('or1_A', 'or1', 0), ('or1_B', 'or1', 0), ('w1', 'and1_A', 1), ('w2', 'and1_B', 2), ('and1', 'or1_A', 3), 
      ('w3', 'or1_B', 4), 
      ('or1', 'sink_in', 0)]

vertex=['source','and1_A', 'and1_B', 'or1_A', 'or1_B', 'w1', 'w2', 'and1', 'w3', 'or1','sink_in']

n=len(vertex)

print n
vertex_dict=dict()

vertex_dict={}

for i in range(1,n+1):
    vertex_dict[vertex[i-1]] = i
    
print vertex_dict

for k in vertex:
    g1.add_vertex(vertex_dict[k],k)



for j in edge:
    v1 = vertex_dict[j[0]]
    v2 = vertex_dict[j[1]]
    weight = j[2]
    g1.add_edge([v1,v2,weight])
    

print g1.graph

print toposort(g1)

print generate_ats(g1,toposort(g1))

reverse_toposort_list= list(toposort(g1))[::-1]

print reverse_toposort_list
print generate_rats_slack(g1,reverse_toposort_list,7)

report_ats_rats_slack(g1)

print g1.get_in_degrees()
    
