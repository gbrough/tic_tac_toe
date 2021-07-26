import random
# define the board positions
board = [' ' for i in range(10)]

#defines the player
player1 = 'X'
computer = 'O'

#print the board
def print_board():
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("------------")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("------------")
    print(board[7] + '|' + board[8] + '|' + board[9])

print_board()
#find if board is full or not
def is_full():
    if ' ' in board:
        return False
    else:
        return True
#who goes first
def who_goes_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'computer'
        
#place a mark on the board
def place_mark(mark, position):
    board[position] = mark

#check if space is free
def is_free(position):
    return board[position] == ' '

#player 1 turn
def player_1_turn():
    position = int(input("Player 1, enter the position you want to place your mark: "))
    place_mark(player1, position)
    print_board()

#computers turn
def computer_turn():
    position = random.randint(0,8)
    place_mark(computer, position)
    print_board()

#check if someone has won
def check_win():
    return (board[1] == board[2] == board[3] == player1 or board[4] == board[5] == board[6] == player1 or board[6] == board[7] == board[8] == board[9] == player1 or board[1] == board[4] == board[7] == player1 or board[2] == board[5] == board[8] == player1 or board[3] == board[6] == board[9] == player1 or board[1] == board[5] == board[9] == player1 or board[3] == board[5] == board[7] == player1 or board[1] == board[2] == board[3] == computer or board[4] == board[5] == board[6] == computer or board[6] == board[7] == board[8] == board[9] == computer or board[1] == board[4] == board[7] == computer or board[2] == board[5] == board[8] == computer or board[3] == board[6] == board[9] == computer or board[1] == board[5] == board[9] == computer or board[3] == board[5] == board[7] == computer)

#start game
while not is_full():
    player_1_turn()
    if check_win():
        print("Player 1 has won")
        break
        
    if check_win():
        print("Computer has won")
        break
    if is_full():
        print("It's a draw")
        break



