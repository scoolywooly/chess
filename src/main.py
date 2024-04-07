# I've used the following tutorial to help me understand how to setup a game with pygame
# https://www.youtube.com/watch?v=AY9MnQ4x3zk&t=1340s


import math
import pygame
from sys import exit
from const import *
from global_variables import *
from game import *

def main(updated_chess_board, holding_a_piece, mouse_pos,):
    # Global Variables
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
    pygame.display.set_caption("Chess")
    
    # some functions are better if I define them in here, so i don't have to import as much varaibles.
    def allow_quit():
        if event.type == pygame.QUIT: # Checks for anytime the player might want to quit the game
                pygame.quit()
                exit()

    
        # Else Nothing happens
        


    # Game Loop
    move = pygame.mixer.Sound("chess-sounds/chess-move.mp3")
    while True:
        
        for event in pygame.event.get():  # any kind of input is handeled here

            mouse = mouse_pos # Bringing global variables to the current scope so Python doesn't have to look outside this scope.
            
            allow_quit()

            if event.type == pygame.MOUSEBUTTONDOWN and holding_a_piece == False: # take a piece

                # Player clicks a piece they want to move
                chess_piece = get_target()
                piece_name = chess_piece[TARGET_PIECE_INDEX]
                piece_position = chess_piece[TARGET_POS_INDEX]


                # update the chess board by returning the changes made with the remove_piece funtion
                updated_chess_board = remove_piece("__",piece_name, piece_position, updated_chess_board)
                floating_piece_info = [piece_name, piece_position]
                holding_a_piece = True

            elif event.type == pygame.MOUSEBUTTONDOWN and holding_a_piece == True: # place a piece

                # Player clicks the square they want to move their piece too,
                # but we must get the information of anything on that square already: "native"
                chess_piece = get_target()
                native_piece = chess_piece[TARGET_PIECE_INDEX]
                new_position = chess_piece[TARGET_POS_INDEX]
                
                # Localizing the piece we moved last event frame.
                moved_piece = floating_piece_info[TARGET_PIECE_INDEX]
                moved_from = floating_piece_info[TARGET_POS_INDEX]


                # Make sure the player is placing the piece in a legal position.
                it_is_a_legal_move = allow_move(moved_from, new_position, moved_piece, updated_chess_board)

                if it_is_a_legal_move:


                    # update the chess board by returning the changes made with the remove_piece funtion
                    updated_chess_board = remove_piece(moved_piece, native_piece, new_position, updated_chess_board)
                    
                else: # If it isn't a legal move, then put the piece back where it came from.
                    updated_chess_board = remove_piece(moved_piece, "__", moved_from, updated_chess_board)
                    
                    
                holding_a_piece = False # We; just put down the piece so we are no longer holding it
                floating_piece_info = []    

        setup_board(updated_chess_board, screen)
        
        chess_board = updated_chess_board
        # Updates everything every frame.
        pygame.display.update()

if __name__ == "__main__":
    main(updated_chess_board, holding_a_piece, mouse_pos)