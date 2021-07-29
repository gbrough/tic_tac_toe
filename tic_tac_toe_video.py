import random

player1 = 'X'
computer = 'O'

#define the board
board = [' ' for i in range(10)]
#print the board
def print_board():
    print('###################')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-------------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-------------')
    print(board[7] + '|' + board[8] + '|' + board[9])

#is the board full
def is_full():
    return ' ' not in board[1:10]

# check if win
def check_win():
  return (board[1] == board[2] == board[3] == player1) or (board[4] == board[5] == board[6] == player1) or (board[7] == board[8] == board[9] == player1) or (board[1] == board[4] == board[7] == player1) or (board[2] == board[5] == board[8] == player1) or (board[3] == board[6] == board[9] == player1) or (board[1] == board[5] == board[9] == player1) or (board[3] == board[5] == board[7] == player1) or (board[1] == board[2] == board[3] == computer) or (board[4] == board[5] == board[6] == computer) or (board[7] == board[8] == board[9] == computer) or (board[1] == board[4] == board[7] == computer) or (board[2] == board[5] == board[8] == computer) or (board[3] == board[6] == board[9] == computer) or (board[1] == board[5] == board[9] == computer) or (board[3] == board[5] == board[7] == computer)

# is space free
def is_free(position):
    return board[position] == ' '

#place marker on board
def place_marker(marker, position):
    board[position] = marker

#player 1 turn
def player_1_turn():
    position = int(input('Player 1, choose a position: '))
    try:
        if is_free(position):
            place_marker(player1, position)
        else:
            print('That position is not free')
            player_1_turn()
    except:
        print('Please choose between 1 and 9')
        player_1_turn()

def who_goes_first():
    if random.randint(0,1) == 0:
        return player1
    else:
        return computer

current_player = who_goes_first()
def switch_player():
  global current_player
  if current_player == player1:
    current_player = computer
  else:
    current_player = player1

#current player turn
def current_player_turn():
    if current_player == player1:
        player_1_turn()
    else:
        computer_turn()

# computer turn
def computer_turn():
    position = random.randint(1,9)
    if is_free(position):
        place_marker(computer, position)
    else:
        computer_turn()

# run the game
def main():
  print('Welcome to Tic Tac Toe!')
  while True:
      print_board()
      switch_player()
      current_player_turn()
      if check_win():
        print(current_player + ' has won!')
        break
      if is_full():
        print('The game is a draw!')
        break
# start the game
main()

