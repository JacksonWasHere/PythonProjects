import pygame
import time
import random
import math

#pygame setup
pygame.init()

#important game variables
display_width=500
display_height=600

black=(0,0,0)
white=(255,255,255)

#tile colors
colors=[(0,0,0),(255,0,0),(0,255,0),(0,0,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255),(255,255,255)]

#create display and game clock
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('2048 Game')
clock = pygame.time.Clock()

#game functions
def rectangle(thingx,thingy,thingw,thingh,color):
    #draws a rectangle
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
def text_objects(text, font):
    #create a text object
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text,x,y,size):
    #get the font
    largeText = pygame.font.Font('freesansbold.ttf',size)

    #create the surface and the area to put it in
    TextSurf, TextRect = text_objects(text, largeText)

    #place the text
    TextRect.center = (x,y)

    #display the text
    gameDisplay.blit(TextSurf, TextRect)
def base_log(base,n):
    if n==0:
        return 0
    return math.log(n)/math.log(base)
def add_tilep(board,x,y,val):
    board[x][y]=val
def add_tile(board):
    #get a random x,y in the board
    x=random.randrange(0,len(board))
    y=random.randrange(0,len(board[0]))
    n=0
    while not board[x][y]==0:
        x=random.randrange(0,len(board))
        y=random.randrange(0,len(board[0]))
        n+=1
        if n>10:
            break;
    #choose the tiles value
    #90%:2
    #10%:4
    random_val=random.randrange(0,100)
    if random_val>=90:
        board[x][y]=4
        return
    board[x][y]=2
def swap_pieces(board,x,y,x1,y1,squished):

    #create variable to see if things change
    changed=False
    if board[x1][y1]==0:
        return changed
    #if 0 move it to new space
    if board[x][y]==0:
        board[x][y]=board[x1][y1]
        board[x1][y1]=0
        #update changed
        changed=True
    #if the same and it hasn't collapsed already then merge
    elif board[x][y]==board[x1][y1] and not ((x,y) in squished):
        board[x][y]=board[x][y]+board[x1][y1]
        board[x1][y1]=0

        squished.append((x,y))
        #update changed
        changed=True
    return changed
def left(board,board_width,board_height,direction):
    #array to see if spot has been collapsed
    collapsed=[]
    #check if stuff changed
    changed=False
    #loop through pieces
    for i in range(board_height-(1 if direction%2==0 else 0)):
        for j in range(board_width):
            #keeps track of it's farthest left place
            end=[(i+1,j),(i,j+1)]
            #loop through all places it could go to
            for x in range(i+1):
                #this is the current piece to check
                possible_x = [i-x, j-x, ]
                newx = possible_x[direction]

                if i==2 and j==3:
                    print(newx)

                #see if it can move to this place
                if board[newx][j]==0 or (board[newx][j]==board[i+1][j] and (not ((newx,j) in collapsed))):
                    #if it can then update the place it'll end
                    end=(newx,j)
                #if it can't move over
                else:
                    #maximize x
                    x=i
                #if we're at the end of the loop
                if x==i:
                    #check if it actually moved
                    if not end==(i+1,j):
                        if i==2 and j==3:
                            print(str(board[i+1][j])+" Move to "+str(end)+" from "+str((i+1,j)))
                        #let us know there was a change
                        changed=True
                        #see if it merges or just goes to a 0
                        if not board[end[0]][end[1]]==0:
                            #add the collapsed point to the list
                            collapsed.append(end)
                        #check how it moved then move it
                        board[end[0]][end[1]] = board[i+1][j] if board[end[0]][end[1]]==0 else board[i+1][j]*2
                        #adjust old position
                        board[i+1][j]=0
                    break
    return changed
def right(board,board_width,board_height):
    collapsed=[]
    changed=False
    for i in range(board_height-1):
        for j in range(board_width):
            for x in range(i+1):
                if not swap_pieces(board,-i+(board_width-2)+x+1,j,-i+(board_width-2),j,collapsed):
                    changed=True
                    break
    return changed
def down(board,board_width,board_height):
    collapsed=[]
    changed=False
    for i in range(board_height):
        for j in range(board_width-1):
            for x in range(j+1):
                if swap_pieces(board,i,-x-1,i,-j+(board_height-2),collapsed):
                    changed=True
                    break
    return changed
def up(board,board_width,board_height):
    collapsed=[]
    changed=False
    for i in range(board_height):
        for j in range(board_width-1):
            for x in range(j+1):
                if swap_pieces(board,i,i+1-x-1,i,j+1,collapsed):
                    changed=True
                    break
    return changed
def game_loop():

    crashed = False

    #setup board
    board_width=4
    board_height=4
    board=[]
    for i in range(board_width):
        board.append([])
        for j in range(board_height):
            board[i].append(0)

    #this code is designed to test functionality

    add_tilep(board,1,0,2)
    add_tilep(board,2,0,4)
    add_tilep(board,3,0,2)

    add_tilep(board,1,1,2)
    add_tilep(board,2,1,2)
    add_tilep(board,3,1,4)

    add_tilep(board,1,2,2)
    add_tilep(board,2,2,2)
    add_tilep(board,3,2,2)

    add_tilep(board,0,3,2)
    add_tilep(board,1,3,4)
    # add_tilep(board,2,3,2)
    add_tilep(board,3,3,2)

    #add start tiles
    #add_tile(board)
    #add_tile(board)

    while not crashed:
        #check all events
        for event in pygame.event.get():
            #check for quit event
            if event.type==pygame.QUIT:
                quit()

            #check for key press
            if event.type==pygame.KEYDOWN:

                #check left movement
                if event.key==pygame.K_LEFT:
                    if left(board,board_width,board_height):
                        add_tile(board)
                if event.key==pygame.K_RIGHT:
                    if right(board,board_width,board_height):
                        add_tile(board)
                if event.key==pygame.K_DOWN:
                    if down(board,board_width,board_height):
                        add_tile(board)
                if event.key==pygame.K_UP:
                    if up(board,board_width,board_height):
                        add_tile(board)

                if event.key==113:
                    pygame.quit()
                    quit()
        #draw stuff
        gameDisplay.fill(white)

        #create tile x,y
        tile_x=0
        tile_y=0

        #size of tiles
        draw_width=display_width/board_width
        draw_height=(display_height-100)/board_height

        #loop through all tiles
        for row in board:
            for column in row:
                #draw a rectangle at the x,y and select a color based on the log of the tile value
                rectangle(tile_x,tile_y,draw_width,draw_height,colors[int(base_log(2,column))])
                #display text
                message_display(str(column),tile_x+draw_width/2,tile_y+draw_height/2,int(draw_width/2))
                #increment the y but keep it within range
                tile_y=(tile_y+draw_height)%(display_height-100)
            #increment x but keep it in range
            tile_x=(tile_x+draw_width)%display_width
        #update the display and set loop delay
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
