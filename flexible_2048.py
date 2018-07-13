import pygame
import time
import random
import math

#pygame setup
pygame.init()

#important game variables
display_width=400
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
def add_tilep(board,x,y):

    #choose the tiles value
    #90%:2
    #10%:4
    random_val=random.randrange(0,100)
    # if random_val>=90:
    #     board[x][y]=4
    #     return
    board[x][y]=2
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
    if board[x][y]==0:
        board[x][y]=board[x1][y1]
        board[x1][y1]=0
    elif board[x][y]==board[x1][y1]:
        board[x][y]=board[x][y]+board[x1][y1]
        board[x1][y1]=0
def left(board,board_width,board_height):
    for i in range(board_height-1):
        for j in range(board_width):
            swap_pieces(board,i,j,i+1,j)
def right(board,board_width,board_height):
    for i in range(board_height-1):
        for j in range(board_width):
            swap_pieces(board,-i-1,j,-i+2,j)
def down(board,board_width,board_height):
    for i in range(board_height):
        for j in range(board_width-1):
            swap_pieces(board,i,-j-1,i,-j+2)
def up(board,board_width,board_height):
    for i in range(board_height):
        for j in range(board_width-1):
            swap_pieces(board,i,j,i,j+1)
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
    add_tilep(board,0,0)
    add_tilep(board,1,0)
    add_tilep(board,2,0)
    add_tilep(board,3,0)
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
                    for x in range(board_width-1):
                        left(board,board_width,board_height)
                    add_tile(board)
                if event.key==pygame.K_RIGHT:
                    for x in range(board_width-1):
                        right(board,board_width,board_height)
                    add_tile(board)
                if event.key==pygame.K_DOWN:
                    for x in range(board_width-1):
                        down(board,board_width,board_height)
                    add_tile(board)
                if event.key==pygame.K_UP:
                    for x in range(board_width-1):
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
