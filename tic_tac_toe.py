import random
# define the board positions
board = [' ' for i in range(10)]

#defines the player
player1 = 'X'
computer = 'O'

#print the board
def print_board():
    print('Next turn')
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("------------")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("------------")
    print(board[7] + '|' + board[8] + '|' + board[9])


#find if board is full or not
def is_full():
        return ' ' not in board[1:10]
#who goes first
def who_goes_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'computer'

#place a marker on the board
def place_mark(mark, position):
    board[position] = mark

#check if space is free
def is_free(position):
    return board[position] == ' '

#player 1 turn
def player_1_turn():
    position = int(input("Player 1, enter the position you want to place your mark: "))
    try:
        if is_free(position):
            place_mark(player1, position)
        else:
            print("This position is already taken")
            player_1_turn()
    except:
        if position < 1 or position > 9:
            print("Please enter a valid position")
            player_1_turn()

#computers turn
def computer_turn():
    if is_free(1):
        place_mark(computer, 1)
    elif is_free(2):
        place_mark(computer, 2)
    elif is_free(3):
        place_mark(computer, 3)
    elif is_free(4):
        place_mark(computer, 4)
    elif is_free(5):
        place_mark(computer, 5)
    elif is_free(6):
        place_mark(computer, 6)
    elif is_free(7):
        place_mark(computer, 7)
    elif is_free(8):
        place_mark(computer, 8)
    elif is_free(9):
        place_mark(computer, 9)

   
#check if someone has won
def check_win():
    return (board[1] == board[2] == board[3] == player1 or board[4] == board[5] == board[6] == player1 or board[6] == board[7] == board[8] == board[9] == player1 or board[1] == board[4] == board[7] == player1 or board[2] == board[5] == board[8] == player1 or board[3] == board[6] == board[9] == player1 or board[1] == board[5] == board[9] == player1 or board[3] == board[5] == board[7] == player1 or board[1] == board[2] == board[3] == computer or board[4] == board[5] == board[6] == computer or board[6] == board[7] == board[8] == board[9] == computer or board[1] == board[4] == board[7] == computer or board[2] == board[5] == board[8] == computer or board[3] == board[6] == board[9] == computer or board[1] == board[5] == board[9] == computer or board[3] == board[5] == board[7] == computer)


#start game
print("Welcome to Tic Tac Toe!")
while True:
    turn = who_goes_first()
    if turn == 'Player 1':
        print_board()
        player_1_turn()
        if check_win() == True:
            print("Player 1 has won")
            break
        else:
            if is_full() == True:
                print("The game is a draw")
                break
            else:
                computer_turn()
                print_board()
                if check_win() == True:
                    print("Computer has won")
                    break
                else:
                    if is_full() == True:
                        print("The game is a draw")
                        break
    else:
        print_board()
        computer_turn()
        print_board()
        if check_win() == True:
            print("Computer has won")
            break
        else:
            if is_full() == True:
                print("The game is a draw")
                break
            else:
                print_board()
                player_1_turn()
                print_board()
                if check_win() == True:
                    print("Player 1 has won")
                    break
                else:
                    if is_full() == True:
                        print("The game is a draw")
                        break

    

  


    




