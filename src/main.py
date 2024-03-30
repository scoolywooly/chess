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

        if event.type == pygame.MOUSEBUTTONDOWN: # When we click the mouse
            chess_board = get_action(current_turn, chess_board)
            

        
    setup_board(chess_board, screen)
    
    # Updates everything every frame.
    pygame.display.update()

