import random
player = 'X'
computer = 'O'

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
def check_win():
  return (board[1] == board[2] == board[3] == player) or \
         (board[4] == board[5] == board[6] == player) or \
         (board[7] == board[8] == board[9] == player) or \
         (board[1] == board[4] == board[7] == player) or \
         (board[2] == board[5] == board[8] == player) or \
         (board[3] == board[6] == board[9] == player) or \
         (board[1] == board[5] == board[9] == player) or \
         (board[3] == board[5] == board[7] == player) or \
         (board[1] == board[2] == board[3] == computer) or \
         (board[4] == board[5] == board[6] == computer) or \
         (board[7] == board[8] == board[9] == computer) or \
         (board[1] == board[4] == board[7] == computer) or \
         (board[2] == board[5] == board[8] == computer) or \
         (board[3] == board[6] == board[9] == computer) or \
         (board[1] == board[5] == board[9] == computer) or \
         (board[3] == board[5] == board[7] == computer)

#is a space free
def is_free(position):
  return board[position] == ' '

#place the marker on the board
def place_marker(marker, position):
  board[position] = marker

#who goes first
def who_goes_first():
  if random.randint(0, 1) == 0:
    return player
  else:
    return computer

#player turn
def player_turn():
  position = int(input('Choose a position: '))
  try:
    if is_free(position):
      place_marker(player, position)
    else:
      print('This position is not free')
      player_turn()
  except:
    if position < 1 or position > 9:
      print('Please choose a number between 1 and 9')
      player_turn()

#computer turn
def computer_turn():
  position  = random.randint(1, 9)
  if is_free(position):
    place_marker(computer, position)
  else:
    computer_turn()

#switch the player and computer
current_player = who_goes_first()
def switch_player():
  global current_player
  if current_player == player:
    current_player = computer
  else:
    current_player = player

#current player
def current_player_turn():
  if current_player == player:
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
    if check_win():
      print_board()
      print(current_player + ' won!')
      break
    if is_full():
      print_board()
      print('Draw!')
      break

#start the game
main()