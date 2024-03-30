mouse_pos = []
moves_made = 0
taken_a_piece = False
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