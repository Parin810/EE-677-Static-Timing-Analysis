'''
Author: Saurav Shandilya, Parin Chheda, Piyush Manavar
Date: 20/11/2017


Name: main.py

Description: 
- Python code to integrate gate connection, graph generation, STA calculation and critical path calculation
- Instruction to run:
- 	in command window type: python main.py --example=X  (where X = 1 or 2, for running example 1 or 2)
	in order to see truthtable: python main.py --example=X --truthtable=1
'''


import logicGate as lg
import allpaths as ap
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import sys


## Plot delay path. Input is a dictionary with value as list of list having set of edges and weight of path
## Critical path is colored in red and shortest path colored in green. Rest path in blue. 
def plot_delay_path(Path_Dict):
    delay_path = nx.Graph()			## name of graph window

    ## figure and window title set
    fig = plt.figure() 				
    fig.canvas.set_window_title('Delay Path') 

    ## markers for legend. 
    red_line = mlines.Line2D([], [], color='r', linewidth=2, label='longest path')
    green_line = mlines.Line2D([], [], color='g', linewidth=2, label='shortest path')
    plt.legend(handles=[red_line,green_line],loc=0)		## loc=0 best fit


    path_weight = []			## store weights
    [path_weight.append(Path_Dict[i][1]) for i in range (len(Path_Dict))  ]
    path_weight = sorted(path_weight)	## sorted 

    ## Loop to generate path and coloring path 
    for i in range (len(Path_Dict)):
        edge_list = Path_Dict[i][0]
        ## Critical path in red
        if (Path_Dict[i][1] == max(path_weight)):	
            for i in range(len(edge_list)):
                delay_path.add_edges_from(edge_list,color='r')
		## shortest path in green               
        elif (Path_Dict[i][1] == min(path_weight)):
            for i in range(len(edge_list)):
                delay_path.add_edges_from(edge_list,color='g')
        ## All other path in blue
        else:
            for i in range(len(edge_list)):
                delay_path.add_edges_from(edge_list,color='b')
        
    ## draw all edegs and give color by extracting color attribute  of edge set above
    edges,colors = zip(*nx.get_edge_attributes(delay_path,'color').items())
    nx.draw(delay_path,edgelist=edges,edge_color=colors,width=3,with_labels=True)

    plt.show()   # show graph window

## Check truth table for example-1
def example_1_truth_table():
	## Generate booleean logic combination for 3 input
	import itertools
	input_value = list(itertools.product([0, 1], repeat=3))

	print "Truth Table ----------------"

	for i in range (len(input_value)):

		## three input wires - for input to gate
		w1 = lg.Source("w1",pos=(0.5,0.1),in1=input_value[i][0])
		w2 = lg.Source("w2",pos=(0.5,-0.1),in1=input_value[i][1])
		w3 = lg.Source("w3",pos=(1.5,-0.1),in1=input_value[i][2])	     

		## sink for taking output
		sink = lg.Sink("sink",pos=(3,0))

		## two gates with delay
		g1 = lg.AndGate("and1",pos=(1,0),delay=2)       # gate delay
		g2 = lg.OrGate("or1",pos=(2,0))
		
		## Connectors and delay
		c1 = lg.Connector(w1,g1,1)		## wire1 to and1_A - wire delay 1
		c2 = lg.Connector(w2,g1,2)		## wire2 to and1_B - wire delay 2
		c3 = lg.Connector(g1,g2,3)		## and1_out to or1_A - wire delay 3
		c4 = lg.Connector(w3,g2,4) 		## wire3 to or1_B - wire delay 4
		c5 = lg.Connector(g2,sink)		## or1_out to sink 

		print "{} {} {} - {}".format(input_value[i][0], input_value[i][1], input_value[i][2], sink.getGateOutput())

## Function to draw gate representation, delay graph, STA calculation, critical path finding of example1
def example_1():	
	w1 = lg.Source("w1",pos=(0.5,0.1))
	w2 = lg.Source("w2",pos=(0.5,-0.1))
	w3 = lg.Source("w3",pos=(1.5,-0.1))

	sink = lg.Sink("sink",pos=(3,0))

	g1 = lg.AndGate("and1",pos=(1,0),delay=2)       # gate delay
	g2 = lg.OrGate("or1",pos=(2,0))
	    
	## Connectors and delay
	c1 = lg.Connector(w1,g1,1)		## wire1 to and1_A - wire delay 1
	c2 = lg.Connector(w2,g1,2)		## wire2 to and1_B - wire delay 2
	c3 = lg.Connector(g1,g2,3)		## and1_out to or1_A - wire delay 3
	c4 = lg.Connector(w3,g2,4) 		## wire3 to or1_B - wire delay 4
	c5 = lg.Connector(g2,sink)		## or1_out to sink 

	## Draw Gate level representation 
	lg.draw_gate_representation()
    
    ## Draw delay graph and get edge and vertex
	lg.draw_delay_graph()
	vertex1,edge1 = lg.get_edge_vertex_for_delay_graph()

	# print "edge delay----"
	# print edge1

	# print "vertex delay----"
	# print vertex1

	## Path calculation
	Path_Dict=ap.path_calculculation (vertex1,edge1)
	print "Main Path Dict =",Path_Dict

    ## Plot critical path
	plot_delay_path(Path_Dict)

## Check truth table for example-1
def example_2_truth_table():
	## Generate booleean logic combination for 3 input
	import itertools
	input_value = list(itertools.product([0, 1], repeat=3))

	print "Truth Table ----------------"

	for i in range (len(input_value)):

		w1 = lg.Source("w1",pos=(0,0.1),in1=input_value[i][0])
		w2 = lg.Source("w2",pos=(0,0),in1=input_value[i][1])
		w3 = lg.Source("w3",pos=(1,-0.1),in1=input_value[i][2])

		sink = lg.Sink("sink",pos=(3,0))

		g1 = lg.AndGate("and1",pos=(1.5,0.5),delay=2)       # gate delay
		g2 = lg.NotGate("not1",pos=(1,0),delay=2)       # gate delay
		g3 = lg.OrGate("or1",pos=(2,0),delay=1)
		g4 = lg.AndGate("and2",pos=(2.5,0),delay=2)       # gate delay
		    
		c1 = lg.Connector(w1,g1,0.15)   # wire to and1_A       # wire delay
		c2 = lg.Connector(w2,g2,0.1)	# wire to not_in
		c3 = lg.Connector(w3,g3,0.1)	# wire to or_A
		c4 = lg.Connector(g2,g1,0.1)	# not_out to and1_B
		c5 = lg.Connector(g2,g3,0.3)	# not_out to or_B
		c6 = lg.Connector(g1,g4,0.2)	# and1_out to and2_A
		c7 = lg.Connector(g3,g4,0.25)	# or_out to and2_B
		c8 = lg.Connector(g4,sink)		# and2_out to sink

		print "{} {} {} - {}".format(input_value[i][0], input_value[i][1], input_value[i][2], sink.getGateOutput())

## Function to draw gate representation, delay graph, STA calculation, critical path finding of example1
def example_2():
	w1 = lg.Source("w1",pos=(0,0.1))
	w2 = lg.Source("w2",pos=(0,0))
	w3 = lg.Source("w3",pos=(1,-0.1))

	sink = lg.Sink("sink",pos=(3,0))

	g1 = lg.AndGate("and1",pos=(1.5,0.5),delay=2)       # gate delay
	g2 = lg.NotGate("not1",pos=(1,0),delay=2)       # gate delay
	g3 = lg.OrGate("or1",pos=(2,0),delay=1)
	g4 = lg.AndGate("and2",pos=(2.5,0),delay=2)       # gate delay
	    
	c1 = lg.Connector(w1,g1,0.15)   # wire to and1_A       # wire delay
	c2 = lg.Connector(w2,g2,0.1)	# wire to not_in
	c3 = lg.Connector(w3,g3,0.1)	# wire to or_A
	c4 = lg.Connector(g2,g1,0.1)	# not_out to and1_B
	c5 = lg.Connector(g2,g3,0.3)	# not_out to or_B
	c6 = lg.Connector(g1,g4,0.2)	# and1_out to and2_A
	c7 = lg.Connector(g3,g4,0.25)	# or_out to and2_B
	c8 = lg.Connector(g4,sink)		# and2_out to sink
	## Draw Gate level representation 
	lg.draw_gate_representation()
	
	## Draw delay graph and get edge and vertex
	lg.draw_delay_graph()
	vertex1,edge1 = lg.get_edge_vertex_for_delay_graph()

	# print "edge delay----"
	# print edge1

	# print "vertex delay----"
	# print vertex1

	Path_Dict=ap.path_calculculation (vertex1,edge1)
	print "Main Path Dict =",Path_Dict

    ## Plot path
	plot_delay_path(Path_Dict)

if __name__ == '__main__':

	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("--truthtable", help="shows truth table of gate")
	parser.add_argument("--example", type=int,help="example number")
	args = parser.parse_args()
	# print args

	if (args.example == 1):
		print args.example
		if args.truthtable:
			example_1_truth_table()
		else:
			example_1()
	
	if (args.example == 2):
		print args.example
		if args.truthtable:
			example_2_truth_table()
		else:
			example_2()
		
	