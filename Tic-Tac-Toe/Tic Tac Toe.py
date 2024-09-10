import random

# Display the Tic-Tac-Toe board
def display_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

# Check if a player has won
def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]             # diagonals
    return any(board[i] == board[j] == board[k] == player for i, j, k in win_conditions)

# Check for a tie
def check_tie(board):
    return all(isinstance(x, str) for x in board)

# Get the computer's move using a basic strategy
def computer_move(board):
    # Winning move
    for i in range(9):
        copy = board[:]
        if isinstance(copy[i], int):
            copy[i] = 'O'
            if check_winner(copy, 'O'):
                return i
    # Block player's winning move
    for i in range(9):
        copy = board[:]
        if isinstance(copy[i], int):
            copy[i] = 'X'
            if check_winner(copy, 'X'):
                return i
    # Take center if available
    if isinstance(board[4], int):
        return 4
    # Take a corner if available
    for i in [0, 2, 6, 8]:
        if isinstance(board[i], int):
            return i
    # Take any available space
    for i in range(9):
        if isinstance(board[i], int):
            return i

# Handle the player's move
def player_move(board):
    while True:
        try:
            move = int(input("Choose your position (0-8): "))
            if move in range(9) and isinstance(board[move], int):
                return move
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Please enter a valid number.")

# Main game loop
def play_game():
    board = list(range(9))
    current_player = random.choice(['you', 'computer'])
    display_board(board)

    while True:
        if current_player == 'you':
            move = player_move(board)
            board[move] = 'X'
            if check_winner(board, 'X'):
                display_board(board)
                print("You win!")
                break
            current_player = 'computer'
        else:
            move = computer_move(board)
            board[move] = 'O'
            print(f"Computer chooses {move}")
            if check_winner(board, 'O'):
                display_board(board)
                print("Computer wins!")
                break
            current_player = 'you'

        display_board(board)

        if check_tie(board):
            print("It's a tie!")
            break

# Start the game
play_game()






































































# #computer is always "O" and user is "X"
# from random import choice
# from helper import check_for_win , select_best_option , block_lose , fill_places , draw_board , draw_line_seperator
# items = [0,1,2,3,4,5,6,7,8]

# def give_input_from_computer():
#     global items 
#     draw_board(items)
#     tmp = items.copy()
#     select_best_option(tmp)
#     if(check_for_win(tmp) == "O"):
#         select_best_option(items)
#         print('computer selected a field')
#         draw_board(items)
#         print('O won')
#         draw_line_seperator()
#         return
#     tmp = items.copy()
#     if(block_lose(tmp) == True):
#         block_lose(items)
#     else:
#         fill_places(items)

#     print('computer selected a field')
#     draw_board(items)
#     draw_line_seperator()
#     if(check_for_win(items) == "X" or check_for_win(items) == "O"):
#         print(f'{check_for_win(items)} won')
#         return 
#     elif(check_for_win(items) == "0-0"):
#         print('game finished but no one won ')
#         return
#     else:
#         give_input_from_user()
# def give_input_from_user():
#     global items 
#     draw_board(items)
#     tmp = input("Choose a number[0-8]: ")
#     if(tmp.isdigit()):
#         chosen_number = int(tmp)
#     else:
#         give_input_from_user()
#     if (chosen_number>=0 and chosen_number<=8):
#         if items[chosen_number] == 'X' or items[chosen_number] ==  'O':
#            print("your chosen place is taken,choose another one")
#            give_input_from_user()
#         else:
#             items[chosen_number] = "X"
#             draw_board(items)  
#             if(check_for_win(items) == "X" or check_for_win(items) == "O"):
#                 print(f'{check_for_win(items)} won')
#                 draw_line_seperator()
#                 return 
#             else:
#                 draw_line_seperator()
#             give_input_from_computer()
#     else:
#         print("invalid input. choose a num between [0-8]")
#         give_input_from_user()
# participants =['player','computer']
# whoseturn = choice(participants)
# if whoseturn == 'player':
#     print("it's your turn to play")
#     give_input_from_user()
# else:
#     print("it's computer's turn to play")
#     give_input_from_computer()
    
