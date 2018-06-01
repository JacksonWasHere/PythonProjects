global board
board=[]
def setup():
    global board
    board=[]
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append("-")
def prettyPrint(grid):
    out = ""
    for i in grid:
        for j in i:
            out+=j
        out+="\n"
    print(out)
def move(x,y,turn):
    if board[x][y]=="-":
        board[x][y]=turn
    else:
        return "Invalid"
    return "valid"
def hasRow(start,turn):
    does=True

    for i in range(3):
        if board[i][start]!=turn:
            does=False

    return does
def hasCol(start,turn):
    does=True

    for i in range(3):
        if board[start][i]!=turn:
            does=False

    return does
def hasDi(start,turn):
    does=True
    for i in range(3):
        if board[i][i]!=turn:
            does=False
    return does
def hasDi2(start,turn):
    does=True
    for i in range(3):
        if board[2-i][i]!=turn:
            does=False
    return does
def didWin(turn):
    hasWon=False
    for i in range(3):
        if hasRow(i,turn):
            return True
        if hasCol(i,turn):
            return True
        if hasDi(i,turn):
            return True
        if hasDi2(i,turn):
            return True
    return False
def endGame(turn,AI):
    print("Good job "+turn+", you won!")
    print("Would you like to play again?")
    pAgain=input("y/n:")
    if pAgain=="q":
        quit()
    if pAgain=="y":
        play("O",AI)
    else:
        start()
def play(turn,AI):
    print("\n")
    prettyPrint(board)
    print("It's "+turn+"\'s turn")
    makingMove=input("Move: ")
    if makingMove=="q":
        quit()
    moveY=(int(makingMove)-1)%3
    moveX=int((int(makingMove)-1)/3)
    if move(moveX,moveY,turn)=="Invalid":
        print("Sorry, that spot is taken.")
        play(turn,AI)
    else:
        if didWin(turn):
            endGame(turn,AI)
        else:
            play("O" if turn=="X" else "X",AI)
def start():
    setup()
    print("Welcome to tic tac toe!")
    print("How would you like to play?")
    print("1:CPU")
    print("2:player vs player")
    mode=input("Choose one: ")
    if mode=="q":
        quit()
    if mode=="2":
        play("O",False)
    if mode=="1":
        play("O",True)
    else:
        print("\nError: mode not found.\n")
        start()
start()
