dict = [
    (" ",8),("#",5),("\n",1),
    (" ",7),("#",7),("\n",1),
    (" ",7),("##O#O##\n",1),(" ",7),("#",1),("@",5),("#\n",1),
    (" ",5),("##$$@@@$$##\n",1),
    (" ",4),("#",1),("$",10),("#\n",1),
    (" ",3),("#",1),("$",12),("##\n",1),
    (" ",3),("#",1),("$",12),("###\n",1),
    (" ",2),("@@#",1),("$",11),("##@\n",1),
    ("@",6),("#",1),("$",7),("#",1),("@",6),("\n",1),
    ("@",7),("#$$$$$#",1),("@",7),("\n",1),
    (" ",2),("@",5),("#",7),("@",5)
]
out=""
for item in dict:
    for i in range(item[1]):
        out+=item[0]
print(out)