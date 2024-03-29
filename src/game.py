# I did this file all by myself
import math
import os
import pygame
from const import *
from global_variables import *

# Low Abstraction
def render_board(surface, current_state=[
        ["br","bn","bb","bq","bk","bb","bn","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):


    cur_square_y_pos = 0
    # a for loop for every square in each row.
    for row in current_state:
        cur_square_x_pos = 0
        for col in row: 
            
           
            cur_square_image = pygame.image.load("chess-images/" + col + ".png") # col refers to "wp" or "_" in the compound list above.
            

            x_pos = [0, 100, 200, 300, 400, 500, 600, 700]
            y_pos = [0, 100, 200, 300, 400, 500, 600, 700]

            

            surface.blit(cur_square_image, (x_pos[cur_square_x_pos], y_pos[cur_square_y_pos]))
            
            cur_square_x_pos += 1
        cur_square_y_pos += 1

def setup_board(board, surface, dark_square=(73, 120, 163), light_square=(212, 224, 197)):

    # The Board
    for row in range(ROWS):
        for col in range(COL):
            if (row + col) % 2 == 0:
                color = (light_square)
            else:
                color = (dark_square)
            
            square = pygame.Surface((SQUARE_W,SQUARE_H))
            square.fill(color)

            # Set the render position of each square to a number that increments by it's initial ammount,
            # Pygame renders sqaures of color from the top left. [0, 75, 150, 225, 300, 375, 450, 525]

            # Eventually, I want to replace the numbers in the list with variables so I can render the screen at different sizes, 
            # but for the purposes of this final project. This will be fine. 
            row_increment = [0, 100, 200, 300, 400, 500, 600, 700]
            col_increment = [0, 100, 200, 300, 400, 500, 600, 700]

            surface.blit(square, (row_increment[row],col_increment[col]))


    

    render_board(surface, board)

def determine_turn(move_count):
    if move_count % 2 != 0: # If it is White's turn
        current_turn = "w"
    else:
        current_turn = "b"
    can_pick_up = True # Somebody's turn just started so teh can_pick_up needs to be true.


def get_mouse_pos():
    mouse_pos = list(pygame.mouse.get_pos())
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    
    return [mouse_x, mouse_y]

def square_clicked(mouse_pos, square_size=100):
    x = mouse_pos[0]
    y = mouse_pos[1]

    # use the floor and ceil to define the edges of the square

    left_edge = math.floor(x / square_size) * square_size
    bottom_edge = math.ceil(y / square_size) * square_size


    # Then I find the cords using the matrix, and a list of rows and columns
    board = [0, 100, 200, 300, 400, 500, 600, 700]
    square_x = 0 # [x, y]
    square_y = 0
    for square in range(len(board)):
        if left_edge == board[square]:
            square_x = square + 1
    for square in range(len(board)):
        if bottom_edge - 100== board[square]: # Its on the bottom, so if i don't minues 100, it looks for an imaginary row that isn't in board
            square_y = square + 1
      
    
    square = [square_x, square_y]

    return square
    
def piece_clicked(square, board=[
        ["br","bn","bb","bq","bk","bb","bn","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):
    x = square[0] - 1
    y = square[1] - 1 # so that the boad doesn't look for an extra row since the computer counts from zero, and the board is made top->down

    target_row = board[y]
    target_piece = target_row[x]

    
    return target_piece, [x+1, y+1]

def remove_piece(piece=str, position=list, board=[
        ["br","bn","bb","bq","bk","bb","bn","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ], replace_with="_"):

    y = position[1] - 1
    x = position[0] - 1 # computers count from zero: So, if its a 1 I need a 0. I shouldn't have to tell you this!
    
    row = board[y] # we use y to get the "clicked_on_row" in the grid/board.
    col = row[x]   # we use x to get the specific piece from the clicked on row.

    if col == piece: # we make sure that the piece that was clicked on is the same as the intersecting square on both row and col
        row[x] = replace_with # we officially replace the row's x index with the "replace_with"
     
    #print(f"{col} =? {piece}")

    return board



# Large Abstraction functions (use low abstraction functions to make larger ones):
def pick_up_piece(board=[
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):


    click_location = get_mouse_pos()
    target_square = square_clicked(click_location)
    target_piece = piece_clicked(target_square)

   #Take off piece from board temporarilly
    updated_chess_board = remove_piece(target_piece[0], target_piece[1], board)


    return [updated_chess_board, target_piece]



def place_piece(placed_piece, board=[
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):
    
    click_location = get_mouse_pos()
    target_square = square_clicked(click_location)
    target_piece = piece_clicked(target_square)

    # Remove empty piece with actual chess piece
    updated_chess_board = remove_piece(target_piece[0], target_piece[1], board, placed_piece)
    # tell game that player can no longer place a piece until another piece is picked up.
    can_pick_up = True


    return updated_chess_board



def get_action(turn="w", board=[
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):
    # If the mouse clicks is even then we pick up a piece
    # If the mouse clicks is odd, then we place a piece

    pass