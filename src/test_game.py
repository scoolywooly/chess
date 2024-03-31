from game import *
import pytest
import pygame

# I have to start the pygame library
pygame.init()

# I have to let the test file know what the board looks like
board_setup = [
        ["br","bn","bb","bq","bk","bb","bn","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","_","_","_","wp","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["wp","wp","wp","wp","_","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]

def test_square_clicked():
    assert square_clicked((240,387), 100) == [3, 4]
    assert square_clicked((10,10), 100) == [1,1] # Top left of the board in chess notation that is A8

def test_piece_clicked():
    assert piece_clicked([1,1], board_setup) == ('br', [1,1])
    assert piece_clicked([1,2], board_setup) == ('bp', [1,2])




test_square_clicked()
test_piece_clicked()

