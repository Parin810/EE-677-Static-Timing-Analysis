

import networkx as ng
import matplotlib.pyplot as plt
import graphclass as g



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
    #print nodes
    #set max values for all rats
    rats = [100]*g1.num_vertices()
    for i in range(0,len(nodes)):
        fanout=g1.get_outneigbours(nodes[i])
        rat = 100
        #if no fanout, rat= cycle time
        if any(fanout)==False:
            #print nodes[i]
            rats[nodes[i]-1]=cycle_time
            g1.graph[nodes[i]].append(cycle_time)
            slack = g1.graph[nodes[i]][-1] - g1.graph[nodes[i]][-2]
            g1.graph[nodes[i]].append(round(slack,2))
            continue
        for k in fanout:
            rat = min(rat,rats[k-1] - g1.get_weight(nodes[i],k))
            #print nodes[i],k,rat
        rats[nodes[i]-1] = round(rat,2)
        g1.graph[nodes[i]].append(rats[nodes[i]-1])
        #compute slack = rat - at at each node 
        slack = g1.graph[nodes[i]][-1] - g1.graph[nodes[i]][-2]
        g1.graph[nodes[i]].append(round(slack,2))
        
    return rats

    
def report_ats_rats_slack(g1,cycletime):
    print "\n"
    print "cycle time :", cycletime
    print "\n"
    for node in g1.get_vertices():
        print "node:", node, ", AAT:", g1.graph[node][-3], ", RAT :" , g1.graph[node][-2], ", slack:", g1.graph[node][-1]
        print "\n"
    
    
    

g1 = g.Graph(12)

for i in range(1,13):
    g1.add_vertex(i)

    
#two three and four are primary inputs, 1 is the source now
g1.add_edge([1,2,0])
g1.add_edge([1,3,0])
g1.add_edge([1,4,0])


g1.add_edge([2,5,1.2])
g1.add_edge([3,6,1.6])
g1.add_edge([5,7,2])
g1.add_edge([6,7,2])

g1.add_edge([7,8,1.5])
g1.add_edge([4,9,1])
g1.add_edge([8,10,3])
g1.add_edge([9,10,3])

g1.add_edge([10,11,1.8])

#sink node
g1.add_edge([11,12,0]) 


#toposort
print toposort(g1)

reverse_toposort_list= list(toposort(g1))[::-1]

## finding out AATs at each node
reverse_toposort_list= list(toposort(g1))[::-1]
print "ats", generate_ats(g1,toposort(g1))

## finding out rats + slack at each node
print "rats", generate_rats_slack(g1,reverse_toposort_list,10)

print g1.graph

#report ats,rats and slack
report_ats_rats_slack(g1,10)
    
