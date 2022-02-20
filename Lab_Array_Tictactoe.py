from random import randrange

board = """
    +-------+-------+-------+
    |       |       |       |
    |   1   |   2   |   3   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   4   |   X   |   6   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   7   |   8   |   9   |
    |       |       |       |
    +-------+-------+-------+
    """
board_array = [[0 for i in range(3)]) for f in range(3)]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.

    print(board)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    try:
        m = int(input("Enter your move: ")) # m = movevalue
        if 0 < m <= 3 and str(m - 1) in board:
        board = board.replace(str(m - 1), "O")
    elif 3 < m <= 6 and str(m - 4) in board:
        board = board.replace(str(m - 4), "O")
    elif 6 < m <= 9 and str(m - 7) in board:
        board = board.replace(str(m - 7), "O")
    else:
        print("Oops! That move is not valid! Please enter a number corresponding to a free field.")
        enter_move(board)
except:
    print("Sorry! I don't understand your move. Please try again!")
    enter_move(board)




def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass


