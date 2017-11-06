import logicGate as lg

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

if __name__ == '__main__':
    check_and()
    check_or()
    check_not()
    check_nand()
    check_nor()