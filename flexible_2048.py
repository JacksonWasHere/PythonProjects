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
def swap_pieces(board,x,y,x1,y1):
    #create variable to see if things change
    changed=False
    #if 0 move it to new space
    if board[x][y]==0:
        board[x][y]=board[x1][y1]
        board[x1][y1]=0
        #update changed
        changed=True
    #if the same then merge
    elif board[x][y]==board[x1][y1]:
        board[x][y]=board[x][y]+board[x1][y1]
        board[x1][y1]=0
        #update changed
        changed=True
    return changed
def left(board,board_width,board_height):
    #loop through pieces
    for i in range(board_height-1):
        for j in range(board_width):
            #loop to find farthest left move location
            for x in range(i+1):
                #if something changed then stop looping
                if swap_pieces(board,x,j,i+1,j):
                    break
def right(board,board_width,board_height):
    for i in range(board_height-1):
        for j in range(board_width):
            for x in range(i+1):
                if swap_pieces(board,-x-1,j,-i+(board_width-2),j):
                    break
def down(board,board_width,board_height):
    for i in range(board_height):
        for j in range(board_width-1):
            for x in range(j+1):
                if swap_pieces(board,i,-x-1,i,-j+(board_height-2)):
                    break
def up(board,board_width,board_height):
    for i in range(board_height):
        for j in range(board_width-1):
            for x in range(j+1):
                if swap_pieces(board,i,x,i,j+1):
                    break
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
    # add_tilep(board,0,0)
    add_tilep(board,1,0,2)
    add_tilep(board,2,0,2)
    add_tilep(board,3,0,4)

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
                    left(board,board_width,board_height)
                    add_tile(board)
                if event.key==pygame.K_RIGHT:
                    right(board,board_width,board_height)
                    add_tile(board)
                if event.key==pygame.K_DOWN:
                    down(board,board_width,board_height)
                    add_tile(board)
                if event.key==pygame.K_UP:
                    up(board,board_width,board_height)
                    add_tile(board)
        #draw stuff
        gameDisplay.fill(white)

        #create tile x,y
        tile_x=0
        tile_y=0

        #loop through all tiles
        for row in board:
            for column in row:
                #draw a rectangle at the x,y and select a color based on the log of the tile value
                rectangle(tile_x,tile_y,100,100,colors[int(base_log(2,column))])
                #display text
                message_display(str(column),tile_x+50,tile_y+50,50)
                #increment the y but keep it within range
                tile_y=(tile_y+100)%400
            #increment x but keep it in range
            tile_x=(tile_x+100)%400
        #update the display and set loop delay
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
