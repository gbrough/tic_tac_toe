def board():
  print("-----------")
  print("|", board[0], "|", board[1], "|", board[2], "|")
  print("-----------")
  print("|", board[3], "|", board[4], "|", board[5], "|")
  print("-----------")
  print("|", board[6], "|", board[7], "|", board[8], "|")
  print("-----------")

board()

#tic_tac_toe.py
#  def board():
#    print("-----------")
#    print("|", board[0], "|", board[1], "|", board[2], "|")
#    print("-----------")
#    print("|", board[3], "|", board[4], "|", board[5], "|")
#    print("-----------")
#    print("|", board[6], "|", board[7], "|", board[8], "|")
#    print("-----------")
# def player_input():
#    marker = ""
#    while not (marker == "X" or marker == "O"):
#        marker = input("Player 1: Do you want to be X or O? ").upper()
#    if marker == "X":
#        return("X", "O")
#    else:
#        return("O", "X")
# def place_marker(board, marker, position):