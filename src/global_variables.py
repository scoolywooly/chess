mouse_pos = []
moves_made = 0
holding_a_piece = False
piece_to_be_removed = "_" # Global variable used all over code to tell what to replace with remove_piece function if not placing down a real piece.
piece_that_was_taken = "_" # Global variable used all over code to tell what piece was taken



# Whatever piece is currently being moved.
current_turn = "w" # By Default the current turn starts on White.

updated_chess_board = [
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["_","_","_","_","_","_","_","_",],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]
    ] # defininf an emptylist, so that it doesn't throw the "not defined" error later