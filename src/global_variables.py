mouse_pos = []
mouse_clicks = 0 # counting variable
moves_made = 0
holding_a_piece = False
old_position = [4,4]
floating_piece_info = [] # once a piece is removed from the board but not yet put onto a new square, it's name and old position will go here..




# Whatever piece is currently being moved.
current_turn = "w" # By Default the current turn starts on White.

updated_chess_board = [
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["__","__","__","__","__","__","__","__",],
    ["__","__","__","__","__","__","__","__",],
    ["__","__","__","__","__","__","__","__",],
    ["__","__","__","__","__","__","__","__",],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ] # defininf an emptylist, so that it doesn't throw the "not defined" error later

chess_set = ["k","q","r","b","n","p"]

controlled_sqaures = {
    "w" : [[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7]], # a list of all the squares that white controlls in the begining of the game
    "b" : [[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3],[7,3],[8,3]]  # a list of all the squares that black controlls in the begining of the game
}

