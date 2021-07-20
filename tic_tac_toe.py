#tic tac toe game
#importing random module
import random

#defining the board
board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#defining the player's markers
player1 = 'X'
player2 = 'O'

#defining the function that prints the board
def print_board():
    print(board[1],'|',board[2],'|',board[3])
    print('----------')
    print(board[4],'|',board[5],'|',board[6])
    print('----------')
    print(board[7],'|',board[8],'|',board[9])

#inserting the markers on the board
def place_marker(board, marker, position):
    board[position] = marker

#check if specified position is free
def check_free(board, position):
    return board[position] == ' '

#check whether the player has won
def check_win(board, marker):
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or #top row
    (board[4] == marker and board[5] == marker and board[6] == marker) or #middle row
    (board[7] == marker and board[8] == marker and board[9] == marker) or #bottom row
    (board[1] == marker and board[4] == marker and board[7] == marker) or #left column
    (board[2] == marker and board[5] == marker and board[8] == marker) or #middle column
    (board[3] == marker and board[6] == marker and board[9] == marker) or #right column
    (board[1] == marker and board[5] == marker and board[9] == marker) or #diagonal
    (board[3] == marker and board[5] == marker and board[7] == marker)) #diagonal

#player1's turn
def player1_turn(board):
    position = 1
    while position not in [1,2,3,4,5,6,7,8,9] or not check_free(board, position):
        position = int(input('Player 1, choose a position: (1-9) '))
    place_marker(board, player1, position)
    
#computer's turn
def computer_turn(board):
    position = 1
    while position not in [1,2,3,4,5,6,7,8,9] or not check_free(board, position):
        position = random.randint(1,9)
    place_marker(board, player2, position)

#randomly choosing who goes first
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#check if the board is full
def check_full(board):
    for i in range(1,10):
        if check_free(board, i):
            return False
    return True

#game play
def play_game():
    print('Welcome to Tic Tac Toe!')
    print('Player 1 is ' + player1 + ' and Player 2 is ' + player2)
    print_board()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True
    while game_on:
        if turn == 'Player 1':
            player1_turn(board)
            print_board()
            if check_win(board, player1):
                print('Congratulations! You won!')
                game_on = False
            else:
                if check_full(board):
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            computer_turn(board)
            print_board()
            if check_win(board, player2):
                print('You lost!')
                game_on = False
            else:
                if check_full(board):
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'
    print('Thanks for playing!')

play_game()