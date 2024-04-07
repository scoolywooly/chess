from game import *
import pytest
import pygame

# I have to start the pygame library
pygame.init()

# I have to let the test file know what the board looks like
board_setup = [ # a fake board for testing purposes
        ["br","bn","bb","bq","bk","bb","bn","br"],
        ["bp","bp","bp","bp","bp","bp","bp","bp"],
        ["_","_","_","_","_","_","_","_",],
        ["_","_","wn","_","_","_","_","_",],
        ["_","_","_","_","_","wp","_","_",],
        ["_","_","_","_","_","_","_","_",],
        ["wp","wp","wp","wp","_","wp","wp","wp"],
        ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ]

def test_square_clicked():
    """
    Get the single digit cordinates of the square based off of the exact mouse position and the size of the square
    and then to store those single digit cords into a list with the first value being the x and the second the y.
    """
    assert square_clicked((240,387), 100) == [3, 4]
    assert square_clicked((10,10), 100) == [1,1] # Top left of the board in chess notation that is A8

def test_piece_clicked():
    """Get the piece and it's single digit cordinates based off of the single digit cordinates of the square its sitting on"""
    assert piece_clicked([1,1], board_setup) == ('br', [1,1])
    assert piece_clicked([1,2], board_setup) == ('bp', [1,2])

def test_get_color():
    """Get the color fo the piece based off it's string"""
    assert get_color("wp") == "w"
    assert get_color("bb") == "b"
    assert get_color("bk") == "b"
    assert get_color("wr") == "w"

def test_compare_lists():
    """USed to make sure my lists that paraody each other for flocalization, 
    or updating the other, or any other reason...are the same"""
    assert compare_lists(["wp","wb","wb","wn"],["wp","wb","wb","wn"]) == True
    assert compare_lists(["wb","br","wk","bk"],["wp","bk","bb","bn"]) == False


pytest.main(["-v", "--tb=line", "-rN", __file__])

"""test_square_clicked()
test_piece_clicked()
test_get_color()
test_too_far_away()
"""