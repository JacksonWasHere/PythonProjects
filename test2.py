global moves
global solution
solution=""
moves=0
def move(a,b):
	global solution
	solution+="["+str(a)+","+str(b)+"],"
def solve(num,start,finish,extra):
	if(num>=1):
		solve(num-1,start,extra,finish)
		move(start,finish)
		global moves
		moves+=1
		solve(num-1,extra,finish,start)
size=input("How Big? ")
solve(int(size),0,2,1)
print("Moves: "+str(moves))
print("Solution: "+solution)
