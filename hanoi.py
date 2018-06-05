from json_manipulation import data_storage
classTest = data_storage("game_data.json")
data=classTest.getData()

global moves
global solution
global compact_solve
compact={
	"[0,1]":"a",
	"[0,2]":"b",
	"[1,0]":"c",
	"[1,2]":"d",
	"[2,0]":"e",
	"[2,1]":"f"
}
solution=""
moves=0

def move(a,b,size):
	global solution
	global compact_solve
	out="["+str(a)+","+str(b)+"]"
	solution+=out+", "

def solve(num,start,finish,extra):
	if(num>=1):
		solve(num-1,start,extra,finish)
		move(start,finish,num)
		global moves
		moves+=1
		solve(num-1,extra,finish,start)

def doIt():
	size=input("How Big? ")
	solve(int(size),0,2,1)

	hasSize=False
	for s in data["games"]["tohan"]:
		if s==size:
			hasSize=True
	compact_solve=str(int(size)-1)+"ab"+str(int(size)-1)+"d"
	data["games"]["tohan"][str(size)]={
		"moves":moves,
		"solution":compact_solve
	}

	classTest.alterData(data)
	classTest.uploadData()
	classTest.refreshData()

	print("Moves: "+str(moves))
	print("Solution: "+solution)
for _ in range(10):
	doIt()
