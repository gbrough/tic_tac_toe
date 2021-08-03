import random

playerLetter = 'X'
computerLetter = 'O'

#define the board
board = [' ' for i in range(10)]

#print the board
def print_board():
  print('#########################')
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('----------')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('----------')
  print(board[7] + '|' + board[8] + '|' + board[9])

#is the board full
def is_full():
  return ' ' not in board[1:10]
 
#check if there is a winner
def check_win(board, letter):
  return (board[1] == board[2] == board[3] == letter) or \
         (board[4] == board[5] == board[6] == letter) or \
         (board[7] == board[8] == board[9] == letter) or \
         (board[1] == board[4] == board[7] == letter) or \
         (board[2] == board[5] == board[8] == letter) or \
         (board[3] == board[6] == board[9] == letter) or \
         (board[1] == board[5] == board[9] == letter) or \
         (board[3] == board[5] == board[7] == letter) or \
         (board[1] == board[2] == board[3] == letter)

#is a space free
def is_free(board, position):
  return board[position] == ' '

#place the marker on the board
def place_marker(board, mark, position):
  board[position] = mark

#who goes first
def who_goes_first():
  if random.randint(0, 1) == 0:
    return playerLetter
  else:
    return computerLetter

#player turn
def player_turn():
  position = int(input('Choose a position: '))
  try:
    if is_free(board, position):
      place_marker(board, playerLetter , position)
    else:
      print('This position is not free')
      player_turn()
  except:
    if position < 1 or position > 9:
      print('Please choose a number between 1 and 9')
      player_turn()

# create a copy of the board
def duplicate_board(board):
  duplicate_board = []
  for i in board:
    duplicate_board.append(i)
  return duplicate_board

#computer turn
def computer_turn():
  #check if computer can win
  position = random.randint(1, 9)
  for i in range(1,10):
    copy = duplicate_board(board)
    if is_free(copy, i):
      place_marker(copy, computerLetter, i)
      if check_win(copy, computerLetter):
        place_marker(board, computerLetter, i)
        return
    else:
      continue
#check if player can win
  for i in range(1,10):
    copy = duplicate_board(board)
    if is_free(copy, i):
      place_marker(copy, playerLetter, i)
      print(f'{copy} copy after place marker')
      if check_win(copy, playerLetter):
        place_marker(board, computerLetter, i)
        print(f'{board} board after place marker')
        return
    else:
      continue

  if is_free(board, position):
   place_marker(board, computerLetter, position)
  else:
    computer_turn()
      
#switch the player and computer
current_player = who_goes_first()
def switch_player():
  global current_player
  if current_player == playerLetter:
    current_player = computerLetter
  else:
    current_player = playerLetter

#current player
def current_player_turn():
  if current_player == playerLetter:
    player_turn()
  else:
    computer_turn()

#run the game
def main():
  print('Welcome to Tic Tac Toe!')

  while True:
    print_board()
    switch_player()
    current_player_turn()
    if check_win(board, current_player):
      print_board()
      print(current_player + ' won!')
      break
    if is_full():
      print_board()
      print('Draw!')
      break

#start the game
main()