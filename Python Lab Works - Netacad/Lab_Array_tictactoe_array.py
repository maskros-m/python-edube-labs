"""
Netacad lab 4.7.2.1. Functions, tuples, exceptions.
"""
import random
import time

# Step 1: Board visualisation:
# building a board which is essentially a two-dimensional list with three elements
board = [[0 for i in range(3)] for f in range(3)]
for i in range(3):
    board[0][i] = i + 1
for j in range(4,7):
    board[1][j-4] = j
for k in range(7, 10):
    board[2][k-7] = k

# computer default's move
board[1][1] = "x"


def display_board(board):
    print(f"""
    +-------+-------+-------+
    |       |       |       |
    |   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
    |       |       |       |
    +-------+-------+-------+
    """)

    
# Step 2s: User's input:
# Will need to break process if no int is found in board.
def enter_move(board):
    m = int(input("Enter your move: "))
    try:
        indx = []
        if 0 < m <= 9:
            for x in board:
                if m in x:
                    indx.append(board.index(x))
                    indx.append(x.index(m))
            a = indx[0]
            b = indx[1]
            board[a][b] = "o"
                
            display_board(board)
            draw_move(board)
            # else:
                # victory_for(board, sign)

        else:
            print("Oops! That move is not valid! Please enter a number corresponding to a free field.")
            enter_move(board)
            

    except:
        print("sorry! i don't understand your move. please try again!")
        enter_move(board)



# Make a list of tuples with row and col as values. Check if the randomised 
# value appears in the list. If yes, delete that element from the list and simultaneously
# adjust the corresponding row-col from board.
    
def make_list_of_free_fields(board):    
    freefields = []
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int) == True:
                freefields.append((row, col))
    return freefields
                
# Step 2b: Computer's move: 
# To be executed after user's move has been registered.
def draw_move(board):
    freefields = make_list_of_free_fields(board)
    i = random.randrange(len(freefields))
    randomx = freefields[i]
    r = randomx[0]
    c = randomx[1]
    board[r][c] = "x"
    del freefields[i]
    
    if freefields != []:
        time.sleep(1)
        display_board(board)
        enter_move(board)
    
    else:
        victory_for(board, sign)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    # *** Error here (for loop finishes before reaching index x = 2):
    you = None
    x = 0
    while x < 3:
        if board[x][0] == board[x][1] == board[x][2] == sign:
            you = True           
        if board[0][x] == board[1][x] == board[2][x] == sign:
            you = True
        if board[x][0] == board[x][1] == board[x][2] != sign:
            you = False           
        if board[0][x] == board[1][x] == board[2][x] != sign:
            you = False
        if (board[0][0] == board[2][2] == 'x' 
            or board[0][2] == board[2][0] == 'x'):
            you = False
        x += 1

    if you == True:
        print("You've won!")
    elif you == False:
        print("Sorry! You've lost!")
    else:
        print("It's a tie!")



            
            
# Backup code (original, still with error)
# def victory_for(board, sign):
    # # The function analyzes the board's status in order to check if 
    # # the player using 'O's or 'X's has won the game
    # # *** Error here:
    # for x in range(len(board)):
        # if (board[x][0] == board[x][1] == board[x][2] == sign \
            # or board[0][x] == board[1][x] == board[2][x] == sign):
            # print("You've won!")
            # break
            
        # elif (board[x][0] == board[x][1] == board[x][2] == 'x' \
            # or board[0][x] == board[1][x] == board[2][x] == 'x' \
            # or board[0][0] == board[2][2] == 'x' \
            # or board[0][2] == board[2][0] == 'x'):
            # print("Sorry! You've lost!")
            # break
        # else:
            # print("It's a tie!")
            # break
sign = 'o'
display_board(board)
enter_move(board)