## Project 4: The Width of a Circle (Part 1) ##
## Fely Magaoay 27278238 ##
## Module 2: USER INTERFACE ##

import project4_logic

#first line: number of rows
#second line: number of columns
        
def number_of_cols_rows():
    ''' this function accepts inputs with integers to set the rows and columns of the board'''
    while True:
        board_col = int(input('')) #int
        board_row = int(input('')) #int
        if 4 <= board_col <= 16 and 4 <= board_col <= 16 and board_col and board_col % 2 == 0 and board_row % 2 == 0:
            return(board_col, board_row)

        else:
            print('Enter even integers between 4 and 16')

#third line: players B or W
def choose_player_first_move():
    '''this function accepts an input str to set the first player'''
    while True:
        first_move = input('') #b or w
        return(first_move)

#fourth line: which color disc will be in top-left position

def choose_player_arrangement():
    '''this function accepts an input str to se the arrangement of the board of which is in the top left'''
    while True:
        choose_player = input('') #b or w
        if choose_player == 'B':
            player1 = choose_player
            player2 = 'W'

            return (player1, player2)
        
        elif choose_player == 'W':
            player1 = choose_player
            player2 = 'B'

            return (player1, player2)

        else:
            print('error')
            
#fifth line: > most discs wins, < fewest discs wins

def most_least_winner():
    '''this function accepts an input if they want the winner to have the most or least scores'''
    while True:
        most_or_least = input('') # > or <
        if most_or_least == '>':
            return most_or_least
        elif most_or_least == '<':
            return most_or_least

def rows_and_columns(board_row, board_col):
    '''this function accepts an input number of rows and columns they want to drop the piece in'''
    while True:
        try:
            row_column = input() #enter row num + row col
            row_column_splitted = row_column.split()
            row = int(row_column_splitted[0]) - 1
            column = int(row_column_splitted[1]) - 1

            if 0 <= row < board_row and 0 <= column < board_col:
                return(row, column)
        except:
            print('INVALID')
            
            
def user_interface():
    print('FULL')
    board_row, board_col = number_of_cols_rows()
    player1, player2 = choose_player_arrangement()
    turn = choose_player_first_move()
    most_or_least = most_least_winner()
    
    game_state = project4_logic.Gamestate(turn, player1, player2, board_col, board_row)

    beginning_board = game_state.beginning_board()
    
    black_score, white_score = game_state.number_of_pieces()
        
    board = game_state.print_board(beginning_board)

    main(game_state, board, most_or_least, board_row, board_col)

def main(game_state, board, most_or_least, board_rows, board_columns):

    while True:
        game_state.copy_game_board(board)
        game_state.locate_similar_piece()
        
        game_state.othello_game_logic()

        if most_or_least == '>':
            if game_state.game_over() == True:
                game_state.copy_game_board(board)
                winner = game_state.winner_with_most_numbers()
                print(winner, 'is the winner')
                quit()

        elif most_or_least == '<':
            if game_state.game_over() == True:
                game_state.copy_board(current_board)
                winner = game_state.winner_with_least_numbers()
                print(winner, 'is the winner')
                quit()

        board_rows, board_columns = rows_and_columns(board_rows, board_columns)


        valid_move_board = game_state.valid_moves(board_rows, board_columns)
        
        game_state.opposite_turn()
        
    
if __name__ == '__main__':
    user_interface()
