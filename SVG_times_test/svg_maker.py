import math
start="<svg id=\"Layer_1\" data-name=\"Layer 1\" xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 520 520\">"
end="</svg>"
global out
out=""

multiplier=2
totalPoints=100
offset=210

def drawStuff(useCol):
  ppoints=[]
  for i in range(totalPoints):
      ppoints.append(drawPoint(200, i, totalPoints))
  for i in range(len(ppoints)):
    cur=ppoints[i]
    nex=ppoints[int(math.floor(i*multiplier%len(ppoints)))]
    global out
    if useCol:
        out+="  "+line(cur[0],cur[1],nex[0],nex[1],i)+"\n"
    else:
        out+="  "+line_black(cur[0],cur[1],nex[0],nex[1])+"\n"

  return start+out+end
def drawPoint(r, currentPoint, totalPoints):

  theta = ((math.pi*2) / totalPoints);
  angle = (theta * currentPoint);

  x = (r * math.cos(angle));
  y = (r * math.sin(angle));
  return [x,y]
def line(x1,y1,x2,y2,num):
    num=float(num)
    return "<line x1=\""+str(x1+offset)+"\" y1=\""+str(y1+offset)+"\" x2=\""+str(x2+offset)+"\" y2=\""+str(y2+offset)+"\" style=\"fill: none;stroke: hsl("+str((num/totalPoints)*360)+",100%,50%);stroke-miterlimit: 10;stroke-width: 1px\"/>"
def line_black(x1,y1,x2,y2):
    return "<line x1=\""+str(x1+offset)+"\" y1=\""+str(y1+offset)+"\" x2=\""+str(x2+offset)+"\" y2=\""+str(y2+offset)+"\" style=\"fill: none;stroke: #000000;stroke-miterlimit: 10;stroke-width: 1px\"/>"
multi=input("multiplier: ")
points=input("number of points: ")
name=raw_input("file: ")
col=input("use color: ")
multiplier=float(multi)
totalPoints=int(points)
line_file = open(name+".svg","w")
line_file.write(drawStuff(col))
