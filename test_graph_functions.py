import networkx as ng
import matplotlib.pyplot as plt
import graphclass as g


def toposort(g1):
	"""Returns a toposorted list"""
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
    """Returns a node indexed ats list,
    index+1=nodenumber"""
    nodes = toposort_list
    print nodes
    ats = [0]*g1.num_vertices()

    for i in range(0,len(nodes)):
        fanin=g1.get_inneigbours(nodes[i])
        mat =0
        if any(fanin)==False:
            ats[nodes[i]-1]=0
            continue
        for k in fanin:
            #print "w",g1.get_weight(k,nodes[i])
            mat = max(mat, ats[k-1]+g1.get_weight(k,nodes[i]))
        ats[nodes[i]-1]=mat
    return ats




g1=g.Graph(2)

print g1.vertices

for i in range(1,6):
    g1.add_vertex(i)

g1.add_edge([1,2,0.5])
g1.add_edge([3,2,1])
g1.add_edge([4,5,2])
g1.add_edge([4,2,3])
g1.add_edge([2,5,0.3])
print g1.graph
g1.draw()

print g1.graph
print toposort(g1)
print generate_ats(g1,toposort(g1))

