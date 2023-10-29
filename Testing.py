import random
import pytest
# change this to make sure we import your file!


##############################
# To install pytest, run pip install pytest
# To run the tests, type in: pytest testing.py

###############################
NUM_COLUMNS = 7
NUM_ROWS = 6

# Your functions (we'll copy this into the connect 4 file once they pass!)
def drop_piece(board, row, column, piece):
    """
    This will set the specified spot in the board to the piece (1 for player 1, 2 for player 2)
    """
    print("TODO!")

def is_valid_location(board, column):
    """
    This function checks to make sure the column (that the player wants
    to drop the piece in) is not full
    """
    print("TODO!")
gui
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
