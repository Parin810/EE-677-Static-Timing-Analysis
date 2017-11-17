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

class LogicGate:
    def __init__(self,n,pos=None):
        self.gateLabel = n       # Gate label - specified by user when instantiating the gate
        self.output = None
        #self.outPin = None
    
    ## Method to allow a user of a gate to ask the gate for its name.
    def getGateLabel(self):
        return self.gateLabel

    ## Method to get logic output of gate. Perform logic computation
    def getGateOutput(self):
        return self.performGateLogic()   # implementation for logic gate in implemented in subclass defined for gate
    

class BinaryGate(LogicGate):
    def __init__(self,n,pos=None,in1=None,in2=None):
        LogicGate.__init__(self,n)
        self.pinA = in1 
        self.pinB = in2 

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
        else:
            if self.pinB == None:
                self.pinB = source
            else:
               print("Cannot Connect: NO EMPTY PINS on this gate")

class UnaryGate(LogicGate):
    def __init__(self,n, pos=None, in1=None):
        LogicGate.__init__(self,n)
        self.pin = in1
    
    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getGateLabel()+"-->"))
        else:
            return self.pin.getFrom().getGateOutput()

    def attachWireFromConnector(self,source):
        # print "print source",source
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
    def __init__(self,n,pos=None,in1=None,in2=None):
        BinaryGate.__init__(self,n,in1,in2)
        node_list.append(n)
        node_info[n] = [pos,'c']
    ## Method for logic implementation
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        return (a and b)

class OrGate(BinaryGate):
    def __init__(self,n,pos=None,in1=None,in2=None):
        BinaryGate.__init__(self,n,in1,in2)
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
    def __init__(self,n,pos=None,in1=None,in2=None):
        BinaryGate.__init__(self,n,in1,in2)
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
    def __init__(self,n,pos=None,in1=None,in2=None):
        BinaryGate.__init__(self,n,in1,in2)
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
    def __init__(self,n,pos=None):
        UnaryGate.__init__(self,n,pos=None)
        node_list.append(n)
        node_info[n] = [pos,'y']
    def performGateLogic(self):

        # return not(self.getPin)
        if self.getPin():
            return 0
        else:
            return 1

## Source - specify input as 1 or 0
class Source(UnaryGate):
    def __init__(self,n,pos=None,in1=None):
        UnaryGate.__init__(self,n,in1)
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

    def __init__(self, srcgate, targetgate):
        self.fromgate = srcgate
        self.togate = targetgate
        
        if (srcgate.getGateLabel(), targetgate.getGateLabel()) not in edge_list:
            edge_list.append((srcgate.getGateLabel(), targetgate.getGateLabel()))
        ## connect wire to target gate input pin
        self.togate.attachWireFromConnector(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

def get_edge_vertex ():
    return node_info.keys(),edge_list

def draw_graph():
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
    plt.show()


if __name__ == '__main__':
    input_value = ([0,0],[0,1],[1,0],[1,1])
    print "AND Gate"
    for i in range (len(input_value)):
        w1 = Source("w1",input_value[i][0])
        w2 = Source("w2",input_value[i][1])
        w3 = Sink("sink")

        g1 = XNOrGate("andGate1")
    
        c1 = Connector(w1,g1)
        c2 = Connector(w2,g1)
        c3 = Connector(g1,w3)    
        print "{} {} - {}".format(input_value[i][0], input_value[i][1], w3.getGateOutput())
    print "Done-----------------"
