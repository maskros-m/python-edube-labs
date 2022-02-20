suboard = []
for inp in range(9):
    surow = input("Enter Sudoku row to check: ")
    surow = surow.replace(" ", "")
    surow = surow.replace("\n", "")
    suboard.append(surow)


board = []
for elem in suboard:
    elem = list(elem)
    board.append(elem)

checklst = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

checkpoint = True
while checkpoint:
    # Check square 3x3
    comparelst = []
    n = 0

    for r in board:
        for row in range(n, n+3):
            for col in range(n, n+3):
                comparelst.append(board[row][col])
        comparelst.sort()
        if comparelst != checklst:
            print("No")
            checkpoint = False
            break
        if comparelst == checklst:
            comparelst = []
            n += 3
        if n > 8:
            break
    if checkpoint == False:
        break

    # Check row:
    
    for r in board:
        t = r[:]
        t.sort()
        if t == checklst:
            continue
        else:
            print("No")
            checkpoint = False
            break
    if checkpoint == False:
        break
        
    # Check column:

    lst = []
    for x in range(9):
        for y in range(9):
            lst.append(board[y][x])
        lst.sort()
        if lst != checklst:
            print("No")
            checkpoint = False
            break
        else:
            lst = []
    if checkpoint == False:
        break
    else:
        print("Yes")
        break