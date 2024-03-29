# me, trying to figure out a minimax algorithm

import math
import random


def get_possible_moves(ran_start, ran_end, depth=1):
    move_possibilites = []
    for i in range(2 * depth):

        item_1 = random.randint(ran_start, ran_end)
        item_2 = item_1
        while item_2 == item_1:
            item_2 = random.randint(ran_start, ran_end)

        move_possibilites.append([item_1, item_2])





    return move_possibilites

moves = get_possible_moves(-9,10,2)
print(moves)







  