def i(e):
    out=""
    d=0
    a=0
    k=0
    t=[0]*512
    while d<len(e):
        c=e[d]
        if c=="+"or c=="-":t[a]=(t[a]+(1 if c=="+"else -1))%256
        elif c==">":a=(a+1)%512
        elif c=="<":a=(a-1)%512
        elif c=="["or c=="]":
            if (t[a]==0 and c=="[")or c=="]":
                l=1
                d+=(1 if c=="["else -1)
                while l>=1:
                    if e[d]=="[":l+=(1 if c=="["else -1)
                    elif e[d]=="]":l-=(1 if c=="["else -1)
                    d+=(1 if c=="["else -1)
                if c=="[":d-=1
        elif c==".":out+=(chr(t[a]))
    elif c==",":t[a]=ord(input("Input: "))
        d+=1
    return [out,t]

def run():
    crashed=False
    while not crashed:
        print("""
#############################################

Welcome to the BrainF*** Interpreter

#############################################

1: Open File
2: Run code
3: What is BF?
        """)
        command = input("select one: ")
        if command=="1":
            open_file()

        elif command=="2":
            run_shell()
        elif command=="3":
            print("""
Here is some important info:
    BF (BrainF***) is an esoteric coding language that uses only +-[]<>.,
    This language is turing complete which means you can do practically any
    computation that you can imagine!
Here's how it works:
    Imagine an infinite tape that is full of 0s,
    each piece of the tape can go up to 255 then it wraps back around to 0.
    each character manipulates the tape in some way.
all the characters
    +: increment this place on the tape
    -: decrement this place on the tape
    >: move right on the tape
    <: move left on the tape
    [: do not enter this unless the current place is > 0
    ]: go back to the corresponding [
    .: print out the ascii character for the current place
    ,: take a byte of user input
""")
            input()

def open_file():
    while True:
        file_name = input("File name: ")
        if file_name=="":
            print("Exiting")
            return
        file = open(file_name+".bf",'r')
        print(i(file.read()))

def run_shell():
    crashed=False
    while not crashed:
        code = input(">>> ")
        print(i(code)[1])
        if code=="":
            print("Exiting shell")
            crashed=True
run()
