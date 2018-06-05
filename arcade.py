import json

class data_storage(object):
    def __init__(self, file_new):
        super(data_storage, self).__init__()
        self.file = file_new
        with open(self.file) as f:
        	data=json.load(f)
        self.data = data
        print(str(self.data)+"\n")
    def getData(self):
        return self.data
    def refreshData(self):
        with open(self.file) as f:
        	data=json.load(f)
        self.data = data
    def alterData(self,new_data):
        self.data=new_data
    def uploadData(self):
        with open(self.file) as f:
        	data=json.load(f)
        self.data = data

class tictactoe(object):
    def __init__(self):
        super(tictactoe, self).__init__()
        self.board=[]
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append("-")

classTest = data_storage("test.json")
def arcade():
    print("-----Welcome to the arcade-----")
