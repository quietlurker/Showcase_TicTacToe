class TicTacToeBoard:
    def __init__(self, board_size):
        self.board_size = board_size
        # without list_name: list = [] pycharm shows warnings if non-int values are put in the list later in the code
        self.board_state: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.print_board()
        self.current_player = "x" # "o"
        self.game_over = False
        self.winner = None

    def print_board(self):
        print(f" {self.board_state[0]} | {self.board_state[1]} | {self.board_state[2]}\n"
              "----------\n"
              f" {self.board_state[3]} | {self.board_state[4]} | {self.board_state[5]}\n"
              "----------\n"
              f" {self.board_state[6]} | {self.board_state[7]} | {self.board_state[8]}\n")

    def update_board(self, player_input):
        if player_input in self.board_state:
            self.board_state[player_input-1] = self.current_player
            if self.current_player == "x":
                self.current_player = "o"
            else:
                self.current_player = "x"

            self.print_board()

            self.check_state()

    def check_state(self):
        # check if no more fields
        # check if someone won
        pass

