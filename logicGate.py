'''
Author: Saurav Shandilya, Parin Chheda, Piyush Manavar
Date: 06/07/2017
Credits: EE-677 source material, Ch-1.13.2. Inheritance: Logic Gates and Circuits on http://interactivepython.org

Name: Implementation of basic Logic gates, source, sink and connectors

Description: 
- Input to logic gate is provided using source block. One source block per input.
- Source is connected to gate using connectors
- Output of logic gate is taken at sink block via connector. One putput per source block.

'''

import networkx as nx 
import matplotlib.pyplot as plt


node_list = []      # create node
edge_list = []      # create edges
node_info = {}      # Store node label, pos and color

node_list_for_delay_graph = []
edge_list_for_delay_graph = []


class LogicGate:
    def __init__(self,n,pos=None, delay=0):
        self.gateLabel = n       # Gate label - specified by user when instantiating the gate
        self.output = None
        self.gatedelay = delay
        #self.outPin = None
    
    ## Method to allow a user of a gate to ask the gate for its name.
    def getGateLabel(self):
        return self.gateLabel

    ## Method to get logic output of gate. Perform logic computation
    def getGateOutput(self):
        return self.performGateLogic()   # implementation for logic gate in implemented in subclass defined for gate
    
    def getGateDelay(self):
        return self.gatedelay

class BinaryGate(LogicGate):
    def __init__(self,n,in1=None,in2=None,pos=None,delay=0):
        LogicGate.__init__(self,n,pos=None,delay=0)
        self.pinA = in1 
        self.pinB = in2 
        # self.delay = delay
        # print "delay ", self.delay
        self.delay = delay
        pin_conn = self.getGateLabel()
        pin_a = pin_conn + "_A"
        pin_b = pin_conn + "_B"
        pin_out = pin_conn 
        
        if pin_a not in node_list_for_delay_graph:
            node_list_for_delay_graph.append(pin_a)
        if pin_b not in node_list_for_delay_graph:
            node_list_for_delay_graph.append(pin_b)
        if pin_out not in node_list_for_delay_graph:
            node_list_for_delay_graph.append(pin_out)

        ## add edges from gate input to out - 2 edges for both input. Add after checking it is not already in added
        if (pin_a,pin_out) not in edge_list_for_delay_graph:
            edge_list_for_delay_graph.append((pin_a, pin_out, self.delay))

        if (pin_b,pin_out) not in edge_list_for_delay_graph:
            edge_list_for_delay_graph.append((pin_b, pin_out, self.delay))

    def getPinA(self):
        if self.pinA == None:
            print "No Connection Made at Pin A"
            # return self.pinA
        else:
            # print "baba A"
            return self.pinA.getFrom().getGateOutput()
    
    def getPinB(self):
        if self.pinB == None:
            print "No Connection Made at Pin B"
            return self.pinB
            # return int(input("Enter Pin B input for gate "+self.getGateLabel()+"-->"))
        else:
            # print "baba B"
            return self.pinB.getFrom().getGateOutput()
    
    def attachWireFromConnector(self,source):
        if self.pinA == None:
            self.pinA = source
            return "A"
        else:
            if self.pinB == None:
                self.pinB = source
                return "B"
            else:
               print("Cannot Connect: NO EMPTY PINS on this gate")
    

class UnaryGate(LogicGate):
    def __init__(self,n,in1=None,pos=None,delay=0):
        LogicGate.__init__(self,n,pos=None,delay=0)
        self.pin = in1

        
        # if self.getGateLabel not in node_list_for_delay_graph:
        #     node_list_for_delay_graph.append(self.getGateLabel)
    
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getGateLabel()+"-->"))
        else:
            return self.pin.getFrom().getGateOutput()

    def attachWireFromConnector(self,source):
        # print "print source",source
        if self.pin == None:
            self.pin = source
            return "in"
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
    def __init__(self,n,in1=None,in2=None, pos=None,delay=0):
        BinaryGate.__init__(self,n,in1,in2,pos,delay)
        node_list.append(n)
        node_info[n] = [pos,'c']
        
    ## Method for logic implementation
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        return (a and b)

class OrGate(BinaryGate):
    def __init__(self,n,in1=None,in2=None,pos=None,delay=0):
        BinaryGate.__init__(self,n,in1,in2,pos,delay)
        node_list.append(n)
        node_info[n] = [pos,'m']
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class XOrGate(BinaryGate):
    def __init__(self,n,in1=None,in2=None,pos=None,delay=0):
        BinaryGate.__init__(self,n,in1,in2,pos,delay)
        node_list.append(n)
        node_info[n] = [pos,'y']
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a ==0:
         if b==0:
            return 0
         else:
             return 1
        else:
         if b==0:
             return 1
         else:
            return 0

class XNOrGate(BinaryGate):
    def __init__(self,n,in1=None,in2=None,pos=None,delay=0):
        BinaryGate.__init__(self,n,in1,in2,pos,delay)
        node_list.append(n)
        node_info[n] = [pos,'blue']
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a ==0:
         if b==0:
            return 1
         else:
             return 0
        else:
         if b==0:
             return 0
         else:
            return 1

class NotGate(UnaryGate):
    def __init__(self,n,pos=None,delay=0):
        UnaryGate.__init__(self,n,pos,delay)
        node_list.append(n)
        node_info[n] = [pos,'y']

        self.delay = delay
        pin_conn = self.getGateLabel()
        pin_a = pin_conn + "_A"
        pin_out = pin_conn 
        # print "and gate delay", delay, 

        # if (pin_a,pin_out) not in edge_list_for_delay_graph:
        #     edge_list_for_delay_graph.append((pin_a, pin_out, self.delay))
    def performGateLogic(self):

        # return not(self.getPin)
        if self.getPin():
            return 0
        else:
            return 1

## Source - specify input as 1 or 0
class Source(UnaryGate):
    def __init__(self,n,in1=None,pos=None,delay=0):
        UnaryGate.__init__(self,n,in1,pos,delay)
        self.pin = in1
        node_list.append(n)
        node_info[n] = [pos,'red']

    def getPin(self):
        if self.pin == None:
            print "Value not Specified"
            return self.pin
        else:
            return self.pin
                    
    def performGateLogic(self):
        if self.getPin():
            return 1
        else:
            return 0           

## Sink - to store output value
class Sink(UnaryGate):
    def __init__(self,n,pos=None):
        UnaryGate.__init__(self,n,pos=None)
        node_list.append(n)
        node_info[n] = [pos,'green']

    def performGateLogic(self):
        if self.getPin():
            return 1
        else:
            return 0

## Connection between gate input/out - source/sink
class Connector:

    def __init__(self, srcgate, targetgate,interconnect_delay=0):
        self.fromgate = srcgate
        self.togate = targetgate
        self.pin_conn = 0
        self.interconnect_delay = interconnect_delay

        self.pin_conn = targetgate.getGateLabel() + "_" +self.togate.attachWireFromConnector(self)
        # print "pin conn - ", self.pin_conn

        if self.pin_conn not in node_list_for_delay_graph:
            node_list_for_delay_graph.append(self.pin_conn)

        if (srcgate.getGateLabel(), targetgate.getGateLabel()) not in edge_list:
            edge_list.append((srcgate.getGateLabel(), targetgate.getGateLabel()))
            

        if (srcgate.getGateLabel(), self.pin_conn) not in edge_list_for_delay_graph:
            # edge_list.append((srcgate.getGateLabel(), targetgate.getGateLabel()))
            edge_list_for_delay_graph.append((srcgate.getGateLabel(), self.pin_conn, self.interconnect_delay))
        ## connect wire to target gate input pin
        

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def get_edge_vertex ():
    return node_info.keys(),edge_list

def get_edge_vertex_for_delay_graph ():
    node_list_for_delay_graph = [i[0] for i in edge_list_for_delay_graph]
    return node_list_for_delay_graph, edge_list_for_delay_graph

def draw_gate_representation():

    fig = plt.figure() 
    fig.canvas.set_window_title('Gate Graph') 

    fixed_positions = {}        # for storing node and its position
    node_list_red = []
    node_list_green = []
    node_list_blue = []
    node_list_c = []
    node_list_m = []
    node_list_y = []

    G=nx.Graph()

    ## add edges
    G.add_edges_from(edge_list) 
    
    ## Extract positions of node
    for keys in node_info.keys():
        fixed_positions[keys] = node_info[keys][0]

        ## create list have node of red color
        if node_info[keys][1] == 'red':
            node_list_red.append(keys)

        ## create list have node of green color
        if node_info[keys][1] == 'green':
            node_list_green.append(keys)

        ## create list have node of blue color
        if node_info[keys][1] == 'blue':
            node_list_blue.append(keys)
        
        ## create list have node of cyan color        
        if node_info[keys][1] == 'c':
            node_list_c.append(keys)

        ## create list have node of magenta color
        if node_info[keys][1] == 'm':
            node_list_m.append(keys)

        ## create list have node of yellow color
        if node_info[keys][1] == 'y':
            node_list_y.append(keys)

    ## Place nodes at desired location
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G,pos=fixed_positions, fixed = fixed_nodes)

    ## draw graph
    nx.draw_networkx(G,pos,nodelist=node_list_green,node_color='green',node_shape='s')
    nx.draw_networkx(G,pos,nodelist=node_list_red,node_color='red')
    nx.draw_networkx(G,pos,nodelist=node_list_blue,node_color='blue')
    nx.draw_networkx(G,pos,nodelist=node_list_c,node_color='c')
    nx.draw_networkx(G,pos,nodelist=node_list_m,node_color='m')
    nx.draw_networkx(G,pos,nodelist=node_list_y,node_color='y')

    ## Plot graph
    plt.show(block=False)

def draw_delay_graph():

    fig = plt.figure() 
    fig.canvas.set_window_title('Delay Graph') 
    G1=nx.Graph()
    edge_list = []

    for i in range(0,len(edge_list_for_delay_graph)):
        edge_list.append(edge_list_for_delay_graph[i][:2])

    # print "edgle list",edge_list

    G1.add_edges_from(edge_list) 
    nx.draw(G1,with_labels = True)
    plt.show()


if __name__ == '__main__':
    input_value = ([0,0],[0,1],[1,0],[1,1])
    print "AND Gate"
    for i in range (len(input_value)):
        w1 = Source("w1",input_value[i][0])
        w2 = Source("w2",input_value[i][1])
        w3 = Sink("sink")

        g1 = AndGate("andGate1")
    
        c1 = Connector(w1,g1)
        c2 = Connector(w2,g1)
        c3 = Connector(g1,w3)    
        print "{} {} - {}".format(input_value[i][0], input_value[i][1], w3.getGateOutput())
    print "Done-----------------"
    # print node_info
    print edge_list_for_delay_graph

