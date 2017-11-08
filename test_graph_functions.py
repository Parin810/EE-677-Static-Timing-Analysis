import networkx as ng
import matplotlib.pyplot as plt
import graphclass as g


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



g1 = g.Graph(5)

for i in range(1,6):
  g1.add_vertex(i)
      
g1.add_edge([1,2])
g1.add_edge([3,2])
g1.add_edge([4,2])
g1.add_edge([4,5])
g1.add_edge([2,5])
g1.draw()
print (toposort(g1))
