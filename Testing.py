import random
import pytest
# change this to make sure we import your file!


##############################
# To install pytest, run pip install pytest
# To run the tests, type in: python -m pytest Testing.py
# To run the tests on MAC, type in: pytest Testing.py

###############################
NUM_COLUMNS = 7
NUM_ROWS = 6

# Your functions (we'll copy this into the connect 4 file once they pass!)
def drop_piece(board, row, column, piece):
    """
    This will set the specified spot in the board to the piece (1 for player 1, 2 for player 2)
    """
    board[row][column] = piece
def is_valid_location(board, column):
    """
    This function checks to make sure the column (that the player wants
    to drop the piece in) is not full
    """
    if board[5][column] == 0:
        return True
    return False
 
def get_next_open_row(board, column):
    """
    Go through the rows (up and down) and find the first opening that's free.
    If you find an opening, return that row number
    """

  
    # 1) Loop through the rows
    
    for i in range(NUM_ROWS):
        
        # 2) If the column the player wants to drop their piece in is open,
        # return that row

        if board[i][column] == 0:
            return i
    

###############################

def is_this_winning_move(board, piece):
    """
    After a player puts down their piece (1 or 2), we want to check if they just made
    a winning move.
    1) Check the horizontal locations, return True if you find a winning movez
    2) Check the vertical locations, return True if you find a winning movez
    3) Check diaganols going up and to the left, return True if you find a winning movez
    4) Check diaganols going up and to the right, return True if you find a winning movez
    Return False if we don't find a winning move.
    """

    # Check the horizontal locations
    for i in range(NUM_ROWS):
        for col_i in range(4):
            if  board[i][col_i] == board[i][col_i + 1] == board[i][col_i + 2] == board[i][col_i + 3] == piece:
                
                return True
                

    # Check the vertical locations
    for i in range(NUM_COLUMNS):
        for row_i in range(3):
            if  board[row_i][i] == board[row_i + 1][i] == board[row_i + 2][i] == board[row_i + 3][i] == piece:

                return True

    # Check diaganols going up and to the left
    for row_i in range(3):
        for col_i in range(4):
            if board[row_i][col_i] == board[row_i + 1][col_i + 1] == board[row_i + 2][col_i + 2] == board[row_i + 3][col_i + 3] == piece:

                return True


     # Check diaganols going up and to the right
    for row_i in range(3, 6):
        for col_i in range(4):
            if board[row_i][col_i] == board[row_i - 1][col_i + 1] == board[row_i - 2][col_i + 2] == board[row_i - 3][col_i + 3] == piece:
    
                return True
   
    return False
############################### 
# Tests (no need to change these!)

def print_board(board):
    """
    This is a helpful provided function for us to view the updated board!
    """
    column_text = "     "
    for i in range(NUM_COLUMNS):
        column_text += f"C{i} "
    print(column_text)
    for row_i in reversed(range(len(board))):
        row = board[row_i]
        current_row = f"R{row_i}: ["
        for col_i in range(len(row)):
            column = row[col_i]
            current_row += str(column)
            if col_i != len(row) - 1:
                current_row += ", "
            else:
                current_row += "]"
        print(current_row)


def test_is_valid_location_1():
    """
    Testing is_valid_location().
    """
    board = [
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
        [0, 0, 0, 0, 0, 0, 0 , 0],
    ]
    assert is_valid_location(board, column=2) == True

def test_is_valid_location_2():
    """
    Testing is_valid_location().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
    print_board(board)
    assert is_valid_location(board, column=1) == False

def test_is_valid_location_2():
    """
    Testing is_valid_location().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1],
        [1, 1, 0, 0, 2, 0, 2],
        [2, 2, 0, 0, 1, 0, 2],
        [2, 1, 0, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
    print_board(board)
    assert is_valid_location(board, column=4) == True

def test_is_valid_location_3():
    """
    Testing is_valid_location().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1],
        [1, 1, 0, 0, 2, 0, 2],
        [2, 2, 0, 0, 1, 0, 2],
        [2, 1, 0, 0, 0, 0, 2],
        [0, 1, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 2],
    ]
    print_board(board)
    assert is_valid_location(board, column=6) == False

def test_drop_piece_1():
    """
    Testing drop_piece().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 2], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 2]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    drop_piece(board=board, row=4, column=0, piece=1)
    assert board[4][0] == 1

def test_drop_piece_2():
    """
    Testing drop_piece().
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 2], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 2]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    drop_piece(board=board, row=0, column=0, piece=2)
    assert board[0][0] == 2


def test_get_next_open_row_1():
    """
    Testing get_next_open_row(board, column).
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 2], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 2]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    row = get_next_open_row(board=board,column=0)
    assert row == 4

def test_get_next_open_row_2():
    """
    Testing get_next_open_row(board, column).
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 2], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 2]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    row = get_next_open_row(board=board,column=2)
    assert row == 0

def test_get_next_open_row_3():
    """
    Testing get_next_open_row(board, column).
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    row = get_next_open_row(board=board,column=6)
    assert row == 5

def test_not_winning_move_1():
    """
    Testing is_this_winning_move(board, piece).
    No winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == False

def test_not_winning_move_2():
    """
    Testing is_this_winning_move(board, piece).
    Not winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 0, 2, 1, 0, 1], #R0
        [1, 1, 0, 0, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 0, 0, 2, 0, 2]
    # R0: [1, 1, 0, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=2)
    assert is_winning_move == False

def test_not_winning_move_3():
    """
    Testing is_this_winning_move(board, piece).
    Not winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 1, 1, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 1, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=2)
    assert is_winning_move == False

def test_horizontal_winning_move_1():
    """
    Testing is_this_winning_move(board, piece).
    Horizontal winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 1, 1, 2, 0, 2], #R1
        [2, 2, 0, 0, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 0, 1, 0, 2]
    # R1: [1, 1, 1, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == True

def test_horizontal_winning_move_2():
    """
    Testing is_this_winning_move(board, piece).
    Horizontal winning move for player 2
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 2, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 2, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=2)
    assert is_winning_move == True

def test_horizontal_winning_move_3():
    """
    Testing is_this_winning_move(board, piece).
    Not horizontal winning move for player 1
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 2, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 2, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == False

def test_vertical_winning_move_1():
    """
    Testing is_this_winning_move(board, piece).
    Not vertical winning move
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 2, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [0, 1, 0, 0, 0, 0, 1], #R4
        [0, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [0, 1, 0, 0, 0, 0, 0]
    # R4: [0, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 2, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == False

def test_vertical_winning_move_2():
    """
    Testing is_this_winning_move(board, piece).
    Vertical winning move for player 2
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 0, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [2, 1, 0, 0, 0, 0, 1], #R4
        [2, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [2, 1, 0, 0, 0, 0, 0]
    # R4: [2, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=2)
    assert is_winning_move == True

def test_vertical_winning_move_3():
    """
    Testing is_this_winning_move(board, piece).
    Not Vertical winning move for player 1
    """
    board = [
       # C0,C1,C2,C3,C4,C5,C6
        [1, 1, 1, 2, 1, 0, 1], #R0
        [1, 1, 2, 1, 2, 0, 2], #R1
        [2, 2, 0, 2, 1, 0, 2], #R2
        [2, 1, 0, 0, 0, 0, 2], #R3
        [2, 1, 0, 0, 0, 0, 1], #R4
        [2, 1, 0, 0, 0, 0, 0], #R5
    ]
    # This board looks like this to us:
    #      C0 C1 C2 C3 C4 C5 C6
    # R5: [2, 1, 0, 0, 0, 0, 0]
    # R4: [2, 1, 0, 0, 0, 0, 1]
    # R3: [2, 1, 0, 0, 0, 0, 2]
    # R2: [2, 2, 0, 2, 1, 0, 2]
    # R1: [1, 1, 2, 1, 2, 0, 2]
    # R0: [1, 1, 1, 2, 1, 0, 1]
    print_board(board)
    is_winning_move = is_this_winning_move(board=board,piece=1)
    assert is_winning_move == False