# I've used the following tutorial to help me understand how to setup a game with pygame
# https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=1340s


import math
import pygame
from sys import exit
from const import *
from global_variables import *
from game import *


# Global Variables
pygame.init()
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
pygame.display.set_caption("Chess")
chess_board = [
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ] 

# some functions are better if I define them in here, so i don't have to import as much varaibles.
def allow_quit():
     if event.type == pygame.QUIT: # Checks for anytime the player might want to quit the game
            pygame.quit()
            exit()

def hold_piece(can_hold_piece, piece=str, mouse_pos=list):
    # Once the remove_piece funciton runs, I recieve a "piece" (str)
    # then I render the piece at the x and y position of the mouse cursor until the mouse clicks again.
    # I need to be called every frame IF the mouse as clicked an odd amount of times.

    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    piece_image = pygame.image.load(piece)
    if can_hold_piece:
        screen.blit(piece_image, (mouse_x, mouse_y))
    # Else Nothing happens
       


# Game Loop
while True:
    
    for event in pygame.event.get():  # any kind of input is handeled here

        mouse = mouse_pos # Bringing global variables to the current scope so Python doesn't have to look outside this scope.
        
        allow_quit()

        if event.type == pygame.MOUSEBUTTONDOWN and taken_a_piece == False: # take a piece
            
            # we find the square clicked, then remove the piece on that square
            click_location = get_mouse_pos()
            target_square = square_clicked(click_location)
            target_piece = piece_clicked(target_square, updated_chess_board)

            if target_piece[TARGET_PIECE_INDEX] == "_":
                
                piece_to_be_removed = target_piece[TARGET_PIECE_INDEX]
            else:
                piece_to_be_removed = "_"

            updated_chess_board = remove_piece(piece_to_be_removed, target_piece[TARGET_PIECE_INDEX],target_piece[TARGET_POS_INDEX], updated_chess_board)

            # prevent taking an empty square and placing an empty square somewhere else, jsut in case the player starts the game by clicking on the empty board.
            
            taken_a_piece = True
            piece_picked_up = str(target_piece[TARGET_PIECE_INDEX])
            print(piece_picked_up)



        elif event.type == pygame.MOUSEBUTTONDOWN and taken_a_piece == True: # place a piece
            
            click_location = get_mouse_pos()
            target_square = square_clicked(click_location)
            target_piece = piece_clicked(target_square, updated_chess_board)

            what_you_clicked = target_piece[TARGET_PIECE_INDEX]
            if what_you_clicked == "_": # If you clicked an empty square
                piece_to_be_removed = "_"

                
            elif what_you_clicked in white_pieces_left: # If you are trying to take a piece
                piece_to_be_removed = target_piece[TARGET_PIECE_INDEX] # sets the piece to be captured
                white_pieces_left.remove(what_you_clicked) # takes the piece you captured out of the remaining list

            elif what_you_clicked in black_pieces_left:
                piece_to_be_removed = target_piece[TARGET_PIECE_INDEX] # sets the piece to be captured
                black_pieces_left.remove(what_you_clicked) # takes the piece you captured out of the remaining list

            else: # If you are just moving pieces
                piece_to_be_removed = target_piece[TARGET_PIECE_INDEX]

            updated_chess_board = remove_piece(piece_picked_up, target_piece[TARGET_PIECE_INDEX],target_piece[TARGET_POS_INDEX], updated_chess_board)

            if target_piece == "_":
                taken_a_piece = False
                


            piece_picked_up = piece_to_be_removed # clear the piece that was taken after being placed
    setup_board(updated_chess_board, screen)
    
    chess_board = updated_chess_board
    # Updates everything every frame.
    pygame.display.update()

