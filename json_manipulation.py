import json
class data_storage(object):
    def __init__(self, file_new):
        super(data_storage, self).__init__()
        self.file = file_new
        with open(self.file) as f:
        	data=json.load(f)
        self.data = data
    def getData(self):
        return self.data
    def refreshData(self):
        with open(self.file) as f:
        	data=json.load(f)
        self.data = data
    def setDataAtPath(self,path,new_value):
        cur_data=self.data
        for i in range(path.count("/")-1):
            print(str(cur_data)+"\n")
            current_place=path[:path.index("/")]
            path=path[path.index("/")+1:]
            cur_data=cur_data[current_place]
        cur_data[path[:path.index("/")]]=2047
    def getDataAtPath(self,path):
        cur_data=self.data
        for i in range(path.count("/")):
            print(str(cur_data)+"\n")
            current_place=path[:path.index("/")]
            path=path[path.index("/")+1:]
            cur_data=cur_data[current_place]
        return cur_data
    def uploadData(self):
        with open(self.file, 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

testing = data_storage("game_data.json")
print("-----"+str(testing.getDataAtPath("games/tohan/11/moves/"))+"-----")
