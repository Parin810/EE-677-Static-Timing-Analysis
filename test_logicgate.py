import logicGate as lg
import allpaths as ap
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


def check_and():
    input_value = ([0,0],[0,1],[1,0],[1,1])
    print "AND Gate"
    for i in range (len(input_value)):
        w1 = lg.Source("w1",input_value[i][0])
        w2 = lg.Source("w2",input_value[i][1])
        w3 = lg.Sink("sink")

        g1 = lg.AndGate("andGate1")
    
        c1 = lg.Connector(w1,g1)
        c2 = lg.Connector(w2,g1)
        c3 = lg.Connector(g1,w3)    
        print "{} {} - {}".format(input_value[i][0], input_value[i][1], w3.getGateOutput())
    print "Done-----------------"

def check_or():
    input_value = ([0,0],[0,1],[1,0],[1,1])
    print "OR Gate"
    for i in range (len(input_value)):
        w1 = lg.Source("w1",input_value[i][0])
        w2 = lg.Source("w2",input_value[i][1])
        w3 = lg.Sink("sink")

        g1 = lg.OrGate("orGate1")
    
        c1 = lg.Connector(w1,g1)
        c2 = lg.Connector(w2,g1)
        c3 = lg.Connector(g1,w3)    
        print "{} {} - {}".format(input_value[i][0], input_value[i][1], w3.getGateOutput())
    print "Done-----------------"

def check_not():
    input_value = (0,1)
    print "Not Gate"
    for i in range (len(input_value)):
        w1 = lg.Source("w1",input_value[i])
        w3 = lg.Sink("sink")

        g1 = lg.NotGate("notGate1")
    
        c1 = lg.Connector(w1,g1)
        c3 = lg.Connector(g1,w3)    
        print "{} - {}".format(input_value[i], w3.getGateOutput())
    print "Done-----------------"

def check_nand():
    input_value = ([0,0],[0,1],[1,0],[1,1])
    print "NAND Gate"
    for i in range (len(input_value)):
        w1 = lg.Source("w1",input_value[i][0])
        w2 = lg.Source("w2",input_value[i][1])
        w3 = lg.Sink("sink")

        g1 = lg.AndGate("andGate1")
        g2 = lg.NotGate("ng1")

        c1 = lg.Connector(w1,g1)
        c2 = lg.Connector(w2,g1)
        c3 = lg.Connector(g1,g2)    
        c4 = lg.Connector(g2,w3)
        print "{} {} - {}".format(input_value[i][0], input_value[i][1], w3.getGateOutput())
    print "Done-----------------"

def check_nor():
    input_value = ([0,0],[0,1],[1,0],[1,1])
    print "NOR Gate"
    for i in range (len(input_value)):
        w1 = lg.Source("w1",input_value[i][0])
        w2 = lg.Source("w2",input_value[i][1])
        w3 = lg.Sink("sink")

        g1 = lg.OrGate("orGate1")
        g2 = lg.NotGate("ng1")

        c1 = lg.Connector(w1,g1)
        c2 = lg.Connector(w2,g1)
        c3 = lg.Connector(g1,g2)    
        c4 = lg.Connector(g2,w3)
        print "{} {} - {}".format(input_value[i][0], input_value[i][1], w3.getGateOutput())
    print "Done-----------------"

def plot_delay_path(Path_Dict):
    delay_path = nx.Graph()

    fig = plt.figure() 
    fig.canvas.set_window_title('Delay Path') 

    red_line = mlines.Line2D([], [], color='r', linewidth=2, label='longest path')
    green_line = mlines.Line2D([], [], color='g', linewidth=2, label='shortest path')

    plt.legend(handles=[red_line,green_line],loc=0)

    path_weight = []
    [path_weight.append(Path_Dict[i][1]) for i in range (len(Path_Dict))  ]
    path_weight = sorted(path_weight,reverse=True)

    for i in range (len(Path_Dict)):
        edge_list = Path_Dict[i][0]
        if (Path_Dict[i][1] == max(path_weight)):
            for i in range(len(edge_list)):
                delay_path.add_edges_from(edge_list,color='r')
        elif (Path_Dict[i][1] == min(path_weight)):
            for i in range(len(edge_list)):
                delay_path.add_edges_from(edge_list,color='g')
        else:
            for i in range(len(edge_list)):
                delay_path.add_edges_from(edge_list,color='b')
        

    edges,colors = zip(*nx.get_edge_attributes(delay_path,'color').items())
    nx.draw(delay_path,edgelist=edges,edge_color=colors,width=3,with_labels=True)

    plt.show()

def check_graph_plot():

    w1 = lg.Source("w1",pos=(0.5,0.1))
    w2 = lg.Source("w2",pos=(0.5,-0.1))
    w3 = lg.Source("w3",pos=(1.5,-0.1))

    sink = lg.Sink("sink",pos=(3,0))

    g1 = lg.AndGate("and1",pos=(1,0),delay=2)       # gate delay
    g2 = lg.AndGate("or1",pos=(2,0))
    
    c1 = lg.Connector(w1,g1,1)          # wire delay
    c2 = lg.Connector(w2,g1,2)
    c3 = lg.Connector(g1,g2,3) 
    c4 = lg.Connector(w3,g2,4) 
    c5 = lg.Connector(g2,sink) 
          
    # print "{} {} - {}".format(input_value[i][0], input_value[i][1], w3.getGateOutput())

    print "Done-----------------"

    lg.draw_gate_representation()
    # vertex,edge = lg.get_edge_vertex()
    vertex1,edge1 = lg.get_edge_vertex_for_delay_graph()
    Path_Dict=ap.path_calculculation (vertex1,edge1)
    print "Main Path Dict =",Path_Dict

    plot_delay_path(Path_Dict)

    # print "vertex ----"
    # print vertex
    # print "edge ----"
    # print edge
    # print lg.node_info
    print "edge delay----"
    print edge1

    print "vertex delay----"
    print vertex1

    lg.draw_delay_graph()


if __name__ == '__main__':
    # check_and()
    # check_or()
    check_not()
    # check_nand()
    # check_nor()

    # check_graph_plot()