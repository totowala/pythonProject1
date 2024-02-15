import numpy as np
import math
import pygame
import sys

RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7
EVEN = 0
ODD = 1

def creat_board():
    board = np.zeros ((6,7))
    return board

def valid (board,position):
    for r in range(ROW_COUNT):
        if board[r][position] == 0:
            return True
    return False

def drop_piece(board,row,col,piece):
    board[row][col] = piece

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print (np.flip(board,0))

def winning_move (board,piece):
    for c in range (COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    for c in range (COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True           
    for c in range(COLUMN_COUNT-3):
	    for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2]==piece and board[r+3][c+3] == piece:
                    return True
    for c in range (COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            
def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
	pygame.display.update()   

    
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 - 5)

board = creat_board()
game_over = False
turn = 0
print(board)
pygame.init()    


width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode (size)
draw_board (board)
pygame.display.update()

myfont = pygame.font.SysFont ('monospace',75)


while not game_over:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
        
         if event.type == pygame.MOUSEMOTION:
              pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
              posx = event.pos[0]
              if turn == 0:
                pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
              else:
                pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
         pygame.display.update()

         if event.type == pygame.MOUSEBUTTONDOWN:
              pygame.draw.rect(screen,RED,(0,0,width,SQUARESIZE))
              if turn == 0:
                   posx = event.pos[0]
                   col = int(math.floor(posx/SQUARESIZE))
                   #col = posx//SQUARESIZE
                   if is_valid_location (board,col):
                        row = get_next_open_row (board,col)
                        drop_piece (board,row,col,1)
                        if winning_move (board,1):
                             label = myfont.render ("player 1 wins!!",1,RED)
                             screen.blit(label,(40,10))
                             game_over = 1
              else:
                   posx = event.pos[0]
                   pygame.draw.rect(screen,RED,(0,0,width,RADIUS))
                   #col = posx//SQUARESIZE
                   col = int(math.floor(posx/SQUARESIZE))
                   if is_valid_location (board,col):
                        row = get_next_open_row (board,col)
                        drop_piece (board,row,col,2)

                        if winning_move (board,2):
                             label = myfont.render ("player 2 wins!!",1,YELLOW)
                             screen.blit(label,(40,10))
                             game_over = 1

              print_board(board)
              draw_board(board)
              turn += 1
              turn = turn % 2

              if game_over:
                   pygame.time.wait(3000)
          
          
 







        

