import sys
import pygame

# Constants we can use in the game!
NUM_COLUMNS = 7
NUM_ROWS = 6

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

def create_board():
    """
    Creates the game board for us!
    NUM_COLUMNS is how openings the board has going side-to-side
    NUM_ROWS is how openings the board has going up and down
    """
    board = []
    for x in range(NUM_ROWS):
        board_level = []
        for y in range(NUM_COLUMNS):
            board_level.append(0)
        board.append(board_level)
    return board

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


def draw_board(board):
    # Draw the board frame (blue background with black holes)
    # (Provided)
    for col in range(NUM_COLUMNS):
        for row in range(NUM_ROWS):
            pygame.draw.rect(screen, BLUE, (col * SQUARE_SIZE, row * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            radius  = SQUARE_SIZE // 2
            circle_x = (col * SQUARE_SIZE) + radius
            circle_y = row * SQUARE_SIZE + radius + SQUARE_SIZE
            pygame.draw.circle(screen, BLACK, (circle_x, circle_y), radius - 2)

    # Update the board with pieces that have been placed
    # TODO
    # Loop over each column
    for col in range(NUM_COLUMNS):
    # Loop over each row
        for row in range(NUM_ROWS):
            radius  = SQUARE_SIZE // 2
            circle_x = (col * SQUARE_SIZE) + radius
            circle_y = (NUM_ROWS - row - 1) * SQUARE_SIZE + radius + SQUARE_SIZE
            if board[row][col] == 1:
                pygame.draw.circle(screen, RED, (circle_x, circle_y), radius - 2)
            
            if board[row][col] == 2:
                pygame.draw.circle(screen, YELLOW, (circle_x, circle_y), radius - 2)
                
    # Draw a circle for each player's piece (refer to the board)


    pygame.display.update()
board = create_board()
gameover = False
# turn will represent whose turn it is ("PLAYER 1" or "PLAYER 2")
turn = "PLAYER 1"

# Pygame set up (we'll uncomment these once we have a working text version!)
pygame.init()
SQUARE_SIZE = 100
SCREEN_WIDTH = NUM_COLUMNS * SQUARE_SIZE
SCREEN_HEIGHT = (NUM_ROWS + 1) * SQUARE_SIZE

size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

draw_board(board)
pygame.display.update()

def player_action(column):
    global turn
    global gameover 
    column_choice = column 
    if turn == "PLAYER 1":
        # While working on the text version, uncomment out these lines
        if is_valid_location(board, column_choice):
            row = get_next_open_row(board, column_choice)
            drop_piece(board, row, column_choice, 1)
            if is_this_winning_move(board, 1):   
                gameover = True 
        turn = "PLAYER 2"
    else:
        # column_choice = int(input("Player 2 choose (0-6)"))
        if is_valid_location(board, column_choice):
            row = get_next_open_row(board, column_choice)
            drop_piece(board, row, column_choice, 2)
            if is_this_winning_move(board, 2):
                gameover = True
        turn = "PLAYER 1"

while not gameover:
    # pygame: (we'll uncomment these once we have a working text version!)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            # This is the section of code which will allow us to see where
            # we're about to drop a piece in

            # 1) Draw a black background/rectangle at the top above the board

            # Get the x_position of where the mouse is
            x_position = event.pos[0]
            pygame.draw.rect(screen, BLACK, (0,0,SCREEN_WIDTH,SQUARE_SIZE))
            if turn == "PLAYER 1":
                pygame.draw.circle(screen, RED, (x_position, 50), 45)
            else:
                pygame.draw.circle(screen, YELLOW, (x_position, 50), 45)
            # Draw the piece (matching the color for the player) where their mouse is   
            # (pygame.draw.circle() may be helpful)

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the x_position of where the mouse is
            x_position = event.pos[0]
            column = (x_position // SQUARE_SIZE)
            

            # Player 1's turn
            column_choice = column
            
            player_action(column)
            

    # You can delete the next 7 lines after you complete the text game!
    

    draw_board(board)
    pygame.display.update()

    if gameover == True:
        # Gameover case, feel free to add to this!
        # As of right now, if a win is detected, it will wait 3 seconds and then close the game.
       
        font = pygame.font.SysFont("yugothicmedium", 60)
        gameover_text = font.render("GAMEOVER",False, (147, 7, 247))
        gameover_text_rect = gameover_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(gameover_text, gameover_text_rect)
        pygame.display.update()
        pygame.time.wait(3000)

        