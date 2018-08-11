from inspect import signature

class gate(object):
    """docstring for gate."""
    def __init__(self, type,ins,outs):
        super(gate, self).__init__()
        self.type = type
        self.inputs = [-1]*ins
        self.outputs = [-1]*outs
        self.current_out = -1
    def add_input(self, new_inputs):
        new_in=self.inputs
        for i in new_inputs:
            new_in[i[1]]=i[0]
        self.inputs=new_in
    def set_output(self, board):
        if -1 in self.inputs:
            self.current_out = -1
        else:
            logic_in=[]
            for i in self.inputs:
                logic_in.append(board[i].current_out)
            self.current_out = self.type(logic_in)
    def get_output(self):
        return self.current_out

def OR(a):
    if a==None:
        return 1
    return a[0] or a[1]
def AND(a):
    if a==None:
        return 1
    return a[0] and a[1]
def XOR(a):
    if a==None:
        return 1
    return not(a[0] and a[1]) and (a[0] or a[1])
def ON(a):
    if a==None:
        return 1
    return True
def OFF(a):
    if a==None:
        return 1
    return False

def add_item(board,num,g_type):
    outs = g_type(None)
    new_g = gate(type,num,outs)
    new_g.set_output(board)
    board.append(new_g)

def logic_sim():
    board=[]
    selected=-1
    add_item(board,0,ON)
    add_item(board,0,OFF)
    add_item(board,2,OR)
    board[2].add_input([(0,0),(1,1)])
    print(board[2].get_output())
logic_sim()
