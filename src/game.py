# I did this file all by myself with some research done at W3schools, 
# and the occasionaly reminder of how list methods worked from Microsoft Codepiliot. All code is my own unless I state otherwise in a comment.

import math
import os
import pygame
from const import *
from global_variables import *

def render_board(surface, current_state=[
        ["br","bn","bb","bq","bk","bb","bn","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):


    cur_square_y_pos = 0
    # a for loop for every square in each row.
    for row in current_state:
        
        cur_square_x_pos = 0
        for col in row: 
            
            # Make sure that any tuples are converted to string, instead of accsesing the entire tuple
            if type(col) == tuple:
                col = str(col[1])
            

            
            cur_square_image = pygame.image.load("chess-images/" + col + ".png") # col refers to "wp" or "__" in the compound list above.
            

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
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):
    x = square[0] - 1
    y = square[1] - 1 # so that the board doesn't look for an extra row since the computer counts from zero, and the board is made top->down

    target_row = board[y]
    target_piece = target_row[x]

    
    return target_piece, [x+1, y+1]

def remove_piece(replace_with, replaced_piece=str, position=list, board=[
        ["br","bn","bb","bq","bk","bb","bn","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["__","__","__","__","__","__","__","__",],
        ["wp","wp","wp","wp","wp","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):

    y = position[1] - 1
    x = position[0] - 1 # computers count from zero: So, if its a 1 I need a 0. I shouldn't have to tell you this!

    row = board[y] # we use y to get the "clicked_on_row" in the grid/board.
    col = row[x]   # we use x to get the specific piece from the clicked on row.

    if col == replaced_piece: # we make sure that the piece that was clicked on is the same as the intersecting square on both row and col
        row[x] = replace_with # we officially replace the row's x index with the "replace_with"
     
    
    
    return board

def get_type_of_move(second_clicked_piece, floating_piece): # Floating piece would be the piece you are holding in your hand.

    # determines whether or not to replace the piece you are removing with blank space, or replace the piece that was moved, and prevents 
    # chess pieces to come back from the dead after they were captured because they were stored in a variable that should be cleared after 
    # every capture.
    if second_clicked_piece and floating_piece == "__": # If I'm moving a piece to an empty square I'm clicking on "__"
        replacement_png = second_clicked_piece

    elif second_clicked_piece and floating_piece != "__": # If I'm capturing a piece then I click on it and it's remvoed from the board, and added to a removed pieces list.
        replacement_png = "__"
        

    else: # Otherwise just replace what was moved from a chess square with an empty chess square.
        replacement_png = floating_piece
    return replacement_png

def get_target():
    click_location = get_mouse_pos()

    target_square = square_clicked(click_location)

    target_piece = piece_clicked(target_square, updated_chess_board)

    return target_piece

def get_color(piece):
    parsed_name = list(piece)
    return parsed_name[TARGET_PIECE_INDEX]

def get_type(piece):
    parsed_name = list(piece)
    return parsed_name[TARGET_TYPE_INDEX]

def all_same_list(my_list):
    return all(same_value == my_list[0] for same_value in my_list)

def compare_lists(list_a, list_b): # Aided with some research done with Microsoft Co-Piliot
    match = False

    for index in range(len(list_a)):
        if list_a[index] == list_b[index]:
            match = True
        else:
            match = False
    
    return match

def add_can_see_square(piece, square_pos, board):
    # I need to see what kind of piece is there. King, Queen, Knight, Pawn etc.
    # I need to see what side the piece is on. White or Black?
    on_square = list(piece)
    color_on_square = on_square[TARGET_PIECE_INDEX]
    type_on_square = on_square[TARGET_TYPE_INDEX]
    square_x = square_pos[X_INDEX]
    square_y = square_pos[Y_INDEX]
    can_see = [] # Squares that can be seen by the piece on that square will be added here, and then sent to the controlled squares dictionary

    if type_on_square == "k": # king can see
        reach = 1
        can_see = [[square_x + reach, square_y], [square_x, square_y], [square_x - reach, square_y],
                   [square_x + reach, square_y + reach], [square_x, square_y + reach], [square_x - reach, square_y + reach],
                   [square_x + reach, square_y - reach], [square_x, square_y - reach], [square_x - reach, square_y - reach]]
        
        

        return can_see
    
    elif type_on_square == "r": # rook can see
        
        look_at_x = square_x
        look_at_y = square_y
        

        distance_right = COL - square_x
        distance_left = square_x - 1
        distance_down = ROWS - square_y
        distance_up = square_y - 1

        total_reach = distance_right + distance_left + distance_down + distance_up
        current_direction = 0


        # adding the squares to the right to can_see list
        for squares_seen in range(total_reach):
            can_see.append([look_at_x, look_at_y])
            
            
            if current_direction == 0: # Looking Right
                look_at_x += 1
            elif current_direction == 1: # Looking Left
                look_at_x -= 1
            elif current_direction == 2: # Looking Down
                look_at_y += 1
            elif current_direction == 3: # Looking Up
                look_at_y -= 1

            

            # change direction
            if squares_seen == distance_right: # done looking right, switch to left
                current_direction += 1
                look_at_x = square_x - 1

            elif squares_seen == distance_left + distance_right: # done looking right and left
                current_direction += 1
                look_at_x = square_x
                look_at_y = square_y + 1

            elif squares_seen == distance_left + distance_down + distance_right: # done looking right, left, and down; switch to up
                current_direction += 1
                look_at_y = square_y + 1
                look_at_x = square_x
            else:
                pass # current direciton is only updated if we have looked at the 

    elif type_on_square == "b": # bishop can see
        look_at_x = square_x
        look_at_y = square_y


        distance_down_right = COL - square_x
        distance_down_left = ROWS - square_y
        distance_up_left = square_x - 1
        distance_up_right = square_y - 1
        # We define the ammount of iterations the for loop has too run

        total_reach = distance_down_right + distance_up_left + distance_down_left + distance_up_right

        direction = 0

        for squares_seen in range(total_reach): # starts with down-right
            can_see.append([look_at_x, look_at_y])

            if direction == 0: # down-right
                look_at_x += 1
                look_at_y += 1
            elif direction == 1: # down-left
                look_at_x -= 1
                look_at_y += 1
            elif direction == 2: # up-left
                look_at_x -= 1
                look_at_y -= 1
            elif direction == 3: #up-right
                look_at_x += 1
                look_at_y -= 1
            
            if squares_seen == distance_down_right: # switch to down-left
                direction += 1
                look_at_x = square_x - 1
                look_at_y = square_y + 1

            elif squares_seen == distance_down_right + distance_down_left: # switch to up-left
                direction += 1
                look_at_x = square_x - 1
                look_at_y = square_y - 1

            elif squares_seen == distance_down_right + distance_down_left + distance_up_left: # switch to up-right
                direction += 1
                look_at_x = square_x + 1
                look_at_y = square_y - 1
            
            else:
                pass
    
    elif type_on_square == "q": # queen can see
            
        look_at_x = square_x
        look_at_y = square_y
        

        distance_right = COL - square_x
        distance_left = square_x - 1
        distance_down = ROWS - square_y
        distance_up = square_y - 1

        total_reach = distance_right + distance_left + distance_down + distance_up
        current_direction = 0


        # adding the squares to the right to can_see list
        for squares_seen in range(total_reach):
            can_see.append([look_at_x, look_at_y])
            
            
            if current_direction == 0: # Looking Right
                look_at_x += 1
            elif current_direction == 1: # Looking Left
                look_at_x -= 1
            elif current_direction == 2: # Looking Down
                look_at_y += 1
            elif current_direction == 3: # Looking Up
                look_at_y -= 1

            

            # change direction
            if squares_seen == distance_right: # done looking right, switch to left
                current_direction += 1
                look_at_x = square_x - 1

            elif squares_seen == distance_left + distance_right: # done looking right and left
                current_direction += 1
                look_at_x = square_x
                look_at_y = square_y + 1

            elif squares_seen == distance_left + distance_down + distance_right: # done looking right, left, and down; switch to up
                current_direction += 1
                look_at_y = square_y + 1
                look_at_x = square_x
            else:
                pass # current direciton is only updated if we have looked at the 
        direction = 0
        look_at_x = square_x
        look_at_y = square_y

        # Add the Bishop range of movement
        for squares_seen in range(total_reach): # starts with down-right
            can_see.append([look_at_x, look_at_y])

            if direction == 0: # down-right
                look_at_x += 1
                look_at_y += 1
            elif direction == 1: # down-left
                look_at_x -= 1
                look_at_y += 1
            elif direction == 2: # up-left
                look_at_x -= 1
                look_at_y -= 1
            elif direction == 3: #up-right
                look_at_x += 1
                look_at_y -= 1
            
            if squares_seen == distance_down_right: # switch to down-left
                direction += 1
                look_at_x = square_x - 1
                look_at_y = square_y + 1

            elif squares_seen == distance_down_right + distance_down_left: # switch to up-left
                direction += 1
                look_at_x = square_x - 1
                look_at_y = square_y - 1

            elif squares_seen == distance_down_right + distance_down_left + distance_up_left: # switch to up-right
                direction += 1
                look_at_x = square_x + 1
                look_at_y = square_y - 1
            
            else:
                pass

    elif type_on_square == "n": # knight can see
        look_at_x = square_x
        look_at_y = square_y

        up = 2 # Directions to make an L shape
        down = -2
        left = -2
        right = 2
        up_increment = 1
        down_increment = -1
        left_increment = 1
        right_increment = -1

         

        move_1 = [look_at_x + right, look_at_y + up_increment]
        move_2 = [look_at_x + right, look_at_y + down_increment]
        move_3 = [look_at_x + left, look_at_y + up_increment]
        move_4 = [look_at_x + left, look_at_y + down_increment]

        move_5 = [look_at_x + left_increment, look_at_y + up]
        move_6 = [look_at_x + right_increment, look_at_y + up]
        move_7 = [look_at_x + left_increment, look_at_y + down]
        move_8 = [look_at_x + right_increment, look_at_y + down]
        

        can_see.append([move_1,move_2,move_3,move_4,move_5,move_6,move_7,move_8])

    elif type_on_square == "p": # pawn can see
        look_at_x = square_x
        look_at_y = square_y
        
        # now it becomes important to know which color the pawn is
        if color_on_square == "w":
            can_see.append([look_at_x + 1, look_at_y - 1],[look_at_x - 1, look_at_y - 1])
        else:
            can_see.append([look_at_x + 1, look_at_y + 1],[look_at_x - 1, look_at_y + 1])
               
    
    can_see.remove(square_pos) # makes sure that the piece doesn't control it's own square so that the opposing king can still capture it
    return can_see

def check_if_controlled(controlling_color=str, desired_move=list):
    """All squares controlled by a piece that prevents a king from moving there, is stored in a dictionary"""
    is_off_limits = False

    enemey_territory = controlled_sqaures[controlling_color]

    if desired_move in enemey_territory:
        is_off_limits = True
    else:
        is_off_limits = False
                                                                                        
    return is_off_limits
    
def check_if_occupied_by_us(my_color=str, desired_move=list, board=list):
    is_occupied = False # Defaults to false

    """I will make lines 214 and 2215 be equal to whether or not the piece is looking at it using the can_look_at() function instead of only
    the desired move."""
    check_x = desired_move[X_INDEX] - 1 # I have to minus 1, because I log the piece's postion counting from 1,
    check_y = desired_move[Y_INDEX] - 1 # counting from 1, whereas python counts from 0 

    row = board[check_y]
    desired_square = row[check_x]

    parsed_piece_name_on_square = list(desired_square)

    if parsed_piece_name_on_square[TARGET_PIECE_INDEX] == my_color: # my_color should only be either "w" or "b"
        is_occupied = True
    
    return is_occupied

def too_far_away(chess_piece, current_position=str, desired_move=list, board=[
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["__","__","__","__","__","__","__","__",],
    ["__","__","__","__","__","__","__","__",],
    ["__","__","__","__","__","__","__","__",],
    ["__","__","__","__","__","__","__","__",],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]):
    too_far = True # Defaults to true, so i don't have to write so many else statements.


    parsed_name = list(chess_piece)
    piece = parsed_name[TARGET_TYPE_INDEX]
    color = parsed_name[TARGET_PIECE_INDEX]
    bad_color = "b" if color == "w" else "w"
    current_x = current_position[X_INDEX]
    current_y = current_position[Y_INDEX]
    desired_x = desired_move[X_INDEX]
    desired_y = desired_move[Y_INDEX]


    if piece == "k": # king
        reach = 1

        horizantil_moves = [current_x + reach, current_x, current_x - reach]
        verticial_moves = [current_y + reach, current_y, current_y - reach]

        if desired_y in verticial_moves:
            if desired_x in horizantil_moves:
                too_far = False
        
    elif piece == "p": # pawn
        reach = 1 # FOR NOW
        horizantil_moves = [current_x + reach, current_x, current_x - reach] # If I didn't check vertical first, this would allow the pawn to move sideways
        verticial_moves = [current_y - 1] if color == "w" else [current_y + 1] # the built in if statement controls whether or not it's black or white.

        if desired_y in verticial_moves:
            if desired_x in horizantil_moves:
                too_far = False
   
    elif piece == "n": # knight
        
        
        up = 2 # Directions to make an L shape
        down = -2
        left = -2
        right = 2
        up_increment = 1
        down_increment = -1
        left_increment = 1
        right_increment = -1

        # chekcing for hte exact position of the desired X and Y in relation to the current position
        if current_y + up == desired_y: # First level, we check the general direction
            if current_x + right_increment == desired_x: # Second level, we move over by one or negative one
                too_far = False
            
            elif current_x + left_increment == desired_x:
                too_far = False

        elif current_y + down == desired_y: # First level, we check the general direction
            if current_x + right_increment == desired_x: # Second level, we move over by one or negative one
                too_far = False
            
            elif current_x + left_increment == desired_x:
                too_far = False
        elif current_x + right == desired_x: # First level, we check the general direction
            if current_y + up_increment == desired_y: # Second level, we move over by one or negative one
                too_far = False
            
            elif current_y + down_increment == desired_y:
                too_far = False
        elif current_x + left == desired_x: # First level, we check the general direction
            if current_y + up_increment == desired_y: # Second level, we move over by one or negative one
                too_far = False
            
            elif current_y + down_increment == desired_y:
                too_far = False
        else:
            too_far = True    

    elif piece == "r": # rook

        # we use incrementing x and y variables to look at all the possible move cordinates, until the cordinates we are looking at are full.
        looking_at_x = 0
        looking_at_y = 0
        squares_in_between = []


        if desired_y == current_y:
            # If moving horizantilly
            space_between = abs(desired_x - current_x)

            for each_move in range(space_between):
                # each move counts the squares in between so it needs to not count from 0
                each_move +=1
                
                
                if desired_x < current_x:
                    looking_at_x = current_x - each_move # moving left
                else:
                    looking_at_x = current_x + each_move # moving right


                row = board[current_y -1]
                square = row[looking_at_x -1] # getting the square we are currently looking at
                square_color = list(square)
                square_color = square_color[0]

                squares_in_between.append(square_color)

                if square == "__" and bad_color not in squares_in_between:
                    too_far = False
                elif square_color == bad_color:
                    too_far = False
                elif square_color == color:
                    too_far = True
                elif square == "__" and bad_color in squares_in_between:
                    too_far = True
                elif square == "__" and color in squares_in_between:
                    too_far = True
                elif square == "__" and color not in squares_in_between:
                    too_far = False
                else:
                    too_far = True
                
                
        elif current_x == desired_x:
            # If moving vertically
            space_between = abs(desired_y - current_y)

            for each_move in range(space_between):
                # each move counts the squares in between so it needs to not count from 0
                each_move +=1

                
                if desired_y < current_y:
                    looking_at_y = current_y - each_move # moving left
                else:
                    looking_at_y = current_y + each_move # moving right


                row = board[looking_at_y-1]
                square = row[current_x-1]
                square_color = list(square)
                square_color = square_color[0]

                squares_in_between.append(square_color)

                if square == "__" and bad_color not in squares_in_between:
                    too_far = False
                elif square_color == bad_color:
                    too_far = False
                elif square_color == color:
                    too_far = True
                elif square == "__" and bad_color in squares_in_between:
                    too_far = True
                elif square == "__" and color in squares_in_between:
                    too_far = True
                elif square == "__" and color not in squares_in_between:
                    too_far = False
                else:
                    too_far = True
                
    elif piece == "q": # queen
        
        # we use incrementing x and y variables to look at all the possible move cordinates, until the cordinates we are looking at are full.
        looking_at_x = 0
        looking_at_y = 0
        squares_in_between = []
        distance = abs(desired_y - current_y)

        # Do some math to findout what are the possible moves using the current_position, and the desired_position
        distance_x = abs(desired_x - current_x)
        distance_y = abs(desired_y - current_y)

        if distance_x == distance_y:
            """If the move is not diagnol from the starting square, then"""
            too_far = False
        

        elif desired_y == current_y:
            # If moving horizantilly
            space_between = abs(desired_x - current_x)

            for each_move in range(space_between):
                # each move counts the squares in between so it needs to not count from 0
                each_move +=1
                
                
                if desired_x < current_x:
                    looking_at_x = current_x - each_move # moving left
                else:
                    looking_at_x = current_x + each_move # moving right


                row = board[current_y -1]
                square = row[looking_at_x -1] # getting the square we are currently looking at
                square_color = list(square)
                square_color = square_color[0]

                squares_in_between.append(square_color)

                if square == "__" and bad_color not in squares_in_between:
                    too_far = False
                elif square_color == bad_color:
                    too_far = False
                elif square_color == color:
                    too_far = True
                elif square == "__" and bad_color in squares_in_between:
                    too_far = True
                elif square == "__" and color in squares_in_between:
                    too_far = True
                elif square == "__" and color not in squares_in_between:
                    too_far = False
                else:
                    too_far = True
                
                
                
        elif current_x == desired_x:
            # If moving vertically
            space_between = abs(desired_y - current_y)

            for each_move in range(space_between):
                # each move counts the squares in between so it needs to not count from 0
                each_move +=1

                
                if desired_y < current_y:
                    looking_at_y = current_y - each_move # moving left
                else:
                    looking_at_y = current_y + each_move # moving right


                row = board[looking_at_y-1]
                square = row[current_x-1]
                square_color = list(square)
                square_color = square_color[0]

                squares_in_between.append(square_color)

                if square == "__" and bad_color not in squares_in_between:
                    too_far = False
                elif square_color == bad_color:
                    too_far = False
                elif square_color == color:
                    too_far = True
                elif square == "__" and bad_color in squares_in_between:
                    too_far = True
                elif square == "__" and color in squares_in_between:
                    too_far = True
                elif square == "__" and color not in squares_in_between:
                    too_far = False
                else:
                    too_far = True
        
            # End of Queen Code

    elif piece == "b": # bishop
        # Do some math to findout what are the possible moves using the current_position, and the desired_position
        distance_x = abs(desired_x - current_x)
        distance_y = abs(desired_y - current_y)

        if distance_x == distance_y:
            """If the move is not diagnol from the starting square, then it is illegal"""
            too_far = False
        else:
            too_far = True
        # End of Bishop Code
            



        


    return too_far

def allow_move(current_position, desired_move=list, piece=str, board=list):
        # desired_move is the x and y position of which square the mouse clicked after selecting a piece, but it won't go through
        # with moving the piece there if desired_move is occupied by a piece of the current player's own color, or if the piece
        # intended to be moved is a king and the desired_move is controlled the enemy.

    allowed = False # Default
    opposing_color = "pass in value"

    parced_piece_str = list(piece)
    my_color = parced_piece_str[TARGET_PIECE_INDEX]

    if my_color == "w":
        opposing_color = "b"
    elif my_color == "b":
        opposing_color = "w"
   
    # Check if one of our own pieces is there already
    its_occupied_by_us = check_if_occupied_by_us(my_color,desired_move,board)

    its_out_of_range = too_far_away(piece, current_position, desired_move, board)

    if its_out_of_range: # Move will not be allowed if its out of the path of movement of the given piece or if its out of range
        allowed = False
    elif its_occupied_by_us:
        allowed = False
    elif its_out_of_range and its_occupied_by_us:
        allowed = False
    elif its_out_of_range == False and its_occupied_by_us == False:
        allowed = True
    


    

    # I ran out of time in this assignment to do the checking or the AI bot, so this project must be and is a literal digital chess board, 
    # made for co-op where both players know the basic rules of Chess and the win conditions of the game.

    """The conditional logic for checking a king goes here goes here.
    It will determine if the King's position is controlled by the enemey, 
    then the only pieces that can be moved will be the King or any piece that can block the check.
    and we determine that by running a for loop that looks at each of the squares from the 
    attacking piece to the king, and seeing if a defending piece can move in place"""

    return allowed