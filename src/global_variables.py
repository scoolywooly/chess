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

controlled_sqaures = {
    "w" : [[1,7],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7]], # a list of all the squares that white controlls in the begining of the game
    "b" : [[1,2],[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[8,2]]  # a list of all the squares that black controlls in the begining of the game
}