import pygame, sys
import numpy as nup
pygame.init()

#variables
WIDTH=480
HEIGHT=480
bg_color=(240,193,113)
line_color=(51, 41, 22)
circle_color=(146, 173, 78)
cross_color=(171, 77, 46)
line_size=10
board_col=3
board_row=3
player=1
circle_rad=48
circle_width=12
cross_width=16
red_line=(214, 49, 55)
game_is_over=False
#creating board
board=nup.zeros((board_row,board_col))

def put_symbol(row, col, player):
    board[row][col]=player

def free_square(row,col):
    if board[row][col]==0:
        return True
    else:
        return False

def is_tie():
    for row in range(board_row):
        for col in range (board_col):
            if board[row][col]==0:
                return False
    return True

#creating playing screen
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Have fun with my TIC-TAC-TOE")
window.fill(bg_color)


def draw_sheet():
    pygame.draw.line(window, line_color, (0,160),(480,160), line_size)
    pygame.draw.line(window, line_color, (0,320), (480, 320), line_size)
    pygame.draw.line(window, line_color, (160, 0), (160,480), line_size)
    pygame.draw.line(window, line_color, (320, 0), (320, 480), line_size)

def draw_symbols():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col]==1:
                pygame.draw.circle(window,circle_color,(int(col*160+80),int(row*160+80)), circle_rad, circle_width)
            elif board[row][col]==2:
                pygame.draw.line(window,cross_color,(col*160+44,row*160+123,),(col*160+123,row*160+44),cross_width)
                pygame.draw.line(window, cross_color, (col * 160 + 44, row * 160 + 44,),
                                 (col * 160 + 123, row * 160 + 123), cross_width)

def check_if_win(player):
    for col in range(board_col):
        if board[0][col]==player and board[1][col]==player and board[2][col]==player:
            vertical_line(col,player)
            return True
    for row in range(board_row):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
            horizontal_line(row,player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        diagonal_line_up(player)
        return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        diagonal_line_down(player)
        return True
    return False

def vertical_line(col,player):
    xplace=col*160+80
    pygame.draw.line(window, red_line, (xplace,10), (xplace, HEIGHT - 10),20)

def horizontal_line(row,player):
    yplace=row*160+80
    pygame.draw.line(window, red_line, (10,yplace), ( WIDTH - 10, yplace),20)

def diagonal_line_up(player):
    pygame.draw.line(window, red_line, (10, HEIGHT-10), (WIDTH - 10, 10), 20)

def diagonal_line_down(player):
    pygame.draw.line(window, red_line, (10,10),(WIDTH - 10, HEIGHT - 10),20)

def play_again():
    global game_is_over
    window.fill(bg_color)
    draw_sheet()
    player=1
    for row in range(board_row):
        for col in range(board_col):
            board[col][row]=0
    game_is_over=False

draw_sheet()


#main program loop
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and not game_is_over:
            mposX=event.pos[0]
            mposY=event.pos[1]
            chosen_row=int(mposY//160)
            chosen_col=int(mposX//160)
            if free_square(chosen_row,chosen_col):
                if player==1:
                    put_symbol(chosen_row,chosen_col,1)
                    if check_if_win(player):
                        game_is_over=True
                    player=2
                elif player==2:
                    put_symbol(chosen_row, chosen_col, 2)
                    if check_if_win(player):
                        game_is_over=True
                    player=1
                draw_symbols()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                play_again()


    pygame.display.update()