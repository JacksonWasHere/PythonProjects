import numpy as np
global ar

def game(width, height):
	global ar
	ar=np.empty(height)
	for i in ar:
		i=np.empty(width)
	for i in range(len(ar)):
		for j in range(len(ar[i])):
			ar[i][j]=false

x=input("X size: ")
y=input("Y Size: ")
game(int(float(x)),int(y))