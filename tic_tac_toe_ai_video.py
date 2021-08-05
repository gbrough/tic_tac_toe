import random

playerLetter = 'X'
computerLetter = 'O'

#define our board
board = [' ' for i in range(10)]

def print_board():
  print('#########################')
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('----------')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('----------')
  print(board[7] + '|' + board[8] + '|' + board[9])

def is_full():
  return ' ' not in board[1:10]
  
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

def is_free(board, position):
  return board[position] == ' '

def place_marker(board, marker, position):
  board[position] = marker

def who_goes_first():
  if random.randint(0, 1) == 0:
    return playerLetter
  else:
    return computerLetter

def player_turn():
  position = input('Choose a position: ')
  try:
    if is_free(board, int(position)):
      place_marker(board, playerLetter, int(position))
    else:
      print('This position is already taken!')
  except:
    print('Please enter a valid position!')
    player_turn()

def duplicate_board(board):
  duplicate_board = []
  for i in board:
    duplicate_board.append(i)
  return duplicate_board

def computer_turn():
  for i in range(1,10):
    copy = duplicate_board(board)
    if is_free(copy, i):
      place_marker(copy, computerLetter, i)
      if check_win(copy, computerLetter):
        place_marker(board, computerLetter, i)
      else:
        continue
  for i in range(1,10):
    copy = duplicate_board(board)
    if is_free(copy, i):
      place_marker(copy, playerLetter, i)
      if check_win(copy, playerLetter):
        place_marker(board, computerLetter, i)
        return
    else:
      continue
  #place in corners, middle, edges
  possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
  corners = [1,3,7,9]
  edges = [2,4,6,8]
  for i in corners:
    if i in possibleMoves:
      return place_marker(board, computerLetter, i)
  if is_free(board, 5):
    return place_marker(board, computerLetter, 5)
  for i in edges:
    if i in possibleMoves:
      return place_marker(board, computerLetter, i)

#run 
def main():
  print('Welcome to Tic Tac Toe!')
  turn = who_goes_first()
  while True:
    if turn == playerLetter:
      print_board()
      player_turn()
      if check_win(board, playerLetter):
        print_board()
        print('You won!')
        break
      elif is_full():
        print_board()
        print('Tie game!')
        break
      else:
        turn = computerLetter
    else:
      computer_turn()
      if check_win(board, computerLetter):
        print_board()
        print('You lost!')
        break
      elif is_full():
        print_board()
        print('Tie game!')
        break
      else:
        turn = playerLetter

main()
