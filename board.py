class TicTacToeBoard:
    def __init__(self, board_size):
        self.board_size = board_size
        # without list_name: list = [] pycharm shows warnings if non-int values are put in the list later in the code
        self.board_state: list = []
        self.create_board()
        self.print_board()
        self.current_player = "x"  # "o"
        self.game_over = False
        self.winner = None

    def create_board(self):
        list_value = 1
        for _ in range(self.board_size ** 2):
            self.board_state.append(list_value)
            list_value += 1

    def print_board(self):
        board = ""
        init_value = 1
        for row in range(self.board_size):
            for column in range(self.board_size):

                # space characters properly - one space if 2char value, two spaces for 1 char values
                if self.board_state[init_value - 1] in ("x", "o", 1, 2, 3, 4, 5, 6, 7, 8, 9):
                    board += f"  {self.board_state[init_value - 1]}  "
                else:
                    board += f" {self.board_state[init_value - 1]}  "

                # add line end at the last column
                if column == self.board_size - 1:
                    board += "\n"
                else:
                    board += "|"
                init_value += 1

            # don't add row separator for last row
            if row != self.board_size - 1:
                # separator size is 6*"-" per column except last one which is 5*"-" so replace it with line end
                for _ in range(self.board_size):
                    board += "------"
                board = board[:-1] + "\n"

        print(board)

    def update_board(self, player_input):
        """
        Updates board with player's choice.
        Checks victory conditions via check_board() and check_if_moves_left() methods.
        Changes player if game continues.
        Prints current board.
        """
        if player_input in self.board_state:
            self.board_state[player_input - 1] = self.current_player
            self.check_board()
            self.check_if_moves_left()
            if not self.winner:
                if self.current_player == "x":
                    self.current_player = "o"
                else:
                    self.current_player = "x"
            self.print_board()

    def check_if_moves_left(self):
        """
        Checks if no more fields left.
        Sets game_over attribute when no more moves left.
        """
        nb_of_x = self.board_state.count("x")
        nb_of_o = self.board_state.count("o")
        if nb_of_x + nb_of_o == self.board_size * self.board_size:
            self.game_over = True

    def check_win(self, list_to_check):
        """
        Helper to check_board.
        Input: list with row or column or diagonal.
        sets winner and game_over if player won.
        """
        if list_to_check.count("x") == self.board_size or list_to_check.count("o") == self.board_size:
            self.winner = self.current_player
            self.game_over = True

    def check_board(self):
        """
        Check victory conditions for rows, columns and diagonals.
        Sets winner and game_over attributes via check_win() method.
        """
        # check if anyone won
        # rows
        row_start_pos = 0
        row_count = 1
        for _ in range(self.board_size):
            # copy value from <row count> row to new list and then check if new list is only x or o
            to_check = [self.board_state[i] for i in range(row_start_pos, self.board_size * row_count)]
            self.check_win(to_check)
            if self.winner:
                # don't check next rows if there's a win in this one
                break
            else:
                row_start_pos += self.board_size
                row_count += 1

        # columns
        # if there's a winning row no need to check columns or diagonals
        if not self.winner:
            column_start_pos = 0
            column_count = 1
            for _ in range(self.board_size):
                # copy value from <columns count> row to new list and then check if new list is only x or o
                to_check = [self.board_state[i] for i in
                            range(column_start_pos, self.board_size * self.board_size, self.board_size)]
                self.check_win(to_check)
                if self.winner:
                    # don't check next columns if there's a win in this one
                    break
                else:
                    column_start_pos += 1
                    column_count += 1

            # diagonals
            # if there's a winning row no need to check columns or diagonals
            if not self.winner:
                start_pos = 0
                # left to right
                step = self.board_size + 1
                for _ in range(2):
                    to_check = [self.board_state[i] for i in range(start_pos, self.board_size * self.board_size, step)]
                    self.check_win(to_check)
                    if self.winner:
                        # don't check other diagonal if there's a win in this one
                        break
                    else:
                        start_pos = start_pos + self.board_size - 1
                        # right to left
                        step = self.board_size - 1
