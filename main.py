from tictactoe_art import logo
from board import TicTacToeBoard

def welcome_message():
    start_message = ("Select game mode:\n"
                     "3: Classic (3x3)\n"
                     "4: 4x4\n"
                     "5: 5x5\n"
                     "0: Quit")
    print(start_message)
    return input("Board size: ")


board_size_int = ""
print(logo)
print("Welcome to tic tac toe! \n")
game_modes = [0, 3, 4, 5,]

init_selection = False

# game init
while not init_selection:
    try:
        board_size_int = int(welcome_message())
    except ValueError:
        print("Select valid option")
    else:
        if board_size_int in game_modes:
            init_selection = True
        else:
            print("Select valid option")


if board_size_int == 0:
    print("OK, bye!")
else:
    # play the game
    game_on = True
    board = TicTacToeBoard(board_size_int)
    while game_on:
        player_choice = input(f"Player {board.current_player}: where do you want to place '{board.current_player}'? ")
        try:
            board.update_board(int(player_choice))
        except ValueError:
            print("Wrong answer")

        # check if anyone one
        if board.winner:
            print(f"Game over! Player {board.current_player} wins!")
            game_on = False
        # check if there's still space on the board
        else:
            if board.game_over:
                game_on = False
                print("Game over! No more moves")

