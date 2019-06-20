## Project 4: The Width of a Circle (Part 1) ##
## Fely Magaoay 27278238 ##
## Module 1: OTHELLO LOGIC ##

NONE = '.'
BLACK = 'B'
WHITE = 'W'

class InvalidMoveError(Exception):
    pass

class Gamestate:

    def __init__(self, turn, player1, player2, board_columns, board_rows):
        self.player1 = player1
        self.player2 = player2
        self.board_columns = board_columns
        self.board_rows = board_rows
        self.turn = turn
        self.moves = []

        self.board = []
        for col in range(self.board_columns):
            self.board.append([])
            for row in range(self.board_rows):
                self.board[-1].append(NONE)
                
    def beginning_board(self):
        '''This function returns the beginning board where there
        are 4 pieces in the middle of the board '''
        self.board[int(self.board_rows/2)-1][int(self.board_columns/2)-1] = self.player1
        self.board[int(self.board_rows/2)][int(self.board_columns/2)] = self.player1
        
        self.board[int(self.board_rows/2)-1][int(self.board_rows/2)] = self.player2
        self.board[int(self.board_rows/2)][int(self.board_rows/2)-1] = self.player2
        
        return self.board


    def copy_game_board(self, board):
        '''This function copies the current game board'''
        current_board = []

        for col in range(self.board_columns):
            current_board.append([])
            for row in range(self.board_rows):
                current_board[-1].append(board[col][row])
        recent_board = self.print_board(current_board)

        return recent_board

    def print_board(self, board):
        '''this function prints the board to be used in the game state'''
        self.black_score, self.white_score = self.number_of_pieces()
        
        print('\n' + 'B: ' + str(self.black_score) + ' ' + 'W: ' + str(self.white_score))
        for row in board:
            for column in row:
                print(column, end = ' ')
            print()

        print('Turn: ' + self.turn)
        return board
        

    def opposite_turn(self) -> str:
        '''this function returns the opposite turn'''
        if self.turn == BLACK:
            return WHITE
        else:
            return BLACK

    def selected_row_col(self, rows, columns):
        '''this function checks if the given row and column are on the board, returns True or False'''
        return 0 <= rows < self.board_rows and 0 <= columns < self.board_columns
        
    def different_piece(self):
        ''' this function switches the pieces back, returning the other color '''
        self.other_color = WHITE
        if self.turn == BLACK:
            self.other_color = WHITE
        elif self.turn == WHITE:
            self.other_color = BLACK

        return self.other_color

    def locate_similar_piece(self):
        '''this function locates the same color of piece in the board'''
        self.list_of_locations = []
        for row in range(self.board_rows):
            for column in range(self.board_columns):
                if self.board[row][column] == self.turn:
                    self.list_of_locations.append([row, column])
            
        
    def othello_game_logic(self):
        '''this function consists of the whole game logic of othello, the lists in these are to be used to flip pieces and determine the valid moves'''
        self.other_color = self.different_piece()
        list_of_adjacent_pieces = []
        self.list_of_validmoves = []
        self.list_of_flipped_pieces = []
        logic_list_of_lists = [[-1,0], [-1,-1], [0,-1],[1,-1],[1,1],[0,1],[-1,1]]
        
        for x , y in logic_list_of_lists:
            for item in self.list_of_locations:
                self.rows_adjacent = item[0] + x
                self.columns_adjacent = item[1] + y

            if self.selected_row_col(self.rows_adjacent, self.columns_adjacent) and self.board[self.rows_adjacent][self.columns_adjacent] == self.other_color:
                    list_of_adjacent_pieces.append([self.rows_adjacent, self.columns_adjacent])

            while self.board[self.rows_adjacent][self.columns_adjacent] == self.other_color:
                self.rows_adjacent = self.rows_adjacent + x
                self.columns_adjacent = self.columns_adjacent + y

            if not self.selected_row_col(self.rows_adjacent, self.columns_adjacent):
                break
            if self.selected_row_col(self.rows_adjacent, self.columns_adjacent):
                if self.board[self.rows_adjacent][self.columns_adjacent] == NONE:
                    self.list_of_validmoves.append([self.rows_adjacent, self.columns_adjacent])

                if self.board[self.rows_adjacent][self.columns_adjacent] == self.turn:
                    while True:
                        self.rows_adjacent = self.rows_adjacent - x
                        self.columns_adjacent = self.columns_adjacent - y

                        if self.board[self.rows_adjacent][self.columns_adjacent] == self.turn:
                            break

        self.list_of_flipped_pieces.append([self.rows_adjacent, self.columns_adjacent])

    def valid_moves(self, board_row, board_col):
        ''' this function checks if the given row and col are invalid or valid'''
        while True:
            if [board_row, board_col] in self.list_of_validmoves:
                print('VALID')
                self.board[board_row][board_col] = self.turn
                self.othello_game_logic()
                board = self.colors_flipped()
                return board

            else:
                print('INVALID')
                break


    def colors_flipped(self) :
        '''this function flips the pieces in the board'''
        for obj in self.list_of_flipped_pieces:
            self.board[obj[0]][obj[1]] = self.turn

        return self.board

    def number_of_pieces(self):
        '''this function checks how many pieces are on the board of that color, in other words the scores'''
        number_of_black = 0
        number_of_white = 0
        for row in self.board:
            for column in row:
                if column == BLACK:
                    number_of_black += 1
                elif column == WHITE:
                    number_of_white += 1

        return (number_of_black, number_of_white)

    def winner_with_most_numbers(self):
        '''this function returns the winner that has most score'''
        winner = BLACK
        if self.game_over():
            if self.black_score > self.white_score:
                winner = BLACK
            elif self.white_score > self.black_score:
                winner = WHITE

        return winner

    def winner_with_least_numbers(self):
        ''' this function returns the winner that has the least score'''
        if self.game_over():
            if self.black_score < self.white_score:
                winner = BLACK

            elif self.white_score < self.black_score:
                winner = WHITE

        return winner


    def game_over(self):
        '''this function checks if the game is over or not'''
        if len(self.list_of_validmoves) == 0:
            return True
        else:
            return False

    def error_with_flipped_pieces(self):
        if len(self.list_of_flipped_pieces) == 0:
            raise InvalidMoveError
                
        
