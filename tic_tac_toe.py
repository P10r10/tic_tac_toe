def rows(s):  # returns a list with the 3 rows in the board
    return [s[0:3], s[3:6], s[6:9]]


def columns(s):  # returns a list with the 3 columns in the board
    return [s[0 + i] + s[3 + i] + s[6 + i] for i in range(3)]


def diagonals(s):  # returns a list with the 2 diagonals in the board
    return [s[0] + s[4] + s[8], s[6] + s[4] + s[2]]


def won(s, side):  # computes the winning condition for side "X" or "O"
    return side * 3 in rows(s) or side * 3 in columns(s) or side * 3 in diagonals(s)


def draw_board(s):
    print("---------")
    for j in range(3):
        print("|", " ".join(c for c in rows(s)[j]), "|")
    print("---------")


def evaluate(s):  # evaluates the state of the game
    if won(s, "X"):
        print("X wins")
    elif won(s, "O"):
        print("O wins")
    elif s.count("_") > 0:
        return False #  Game not finished
    else:
        print("Draw")
    return True


def get_move():
    while True:
        move = input()
        if not move[0].isdigit() or not move[2].isdigit():
            print("You should enter numbers!")
            continue
        r, c = int(move[0]), int(move[2])
        if r < 1 or r > 3 or c < 1 or c > 3:
            print("Coordinates should be from 1 to 3!")
            continue
        return r, c


def move(board, side):
    while True:
        row, col = get_move()
        idx = 3 * (row - 1) + (col - 1) #  computes index based on row and col
        if board[idx] != "_":
            print("This cell is occupied! Choose another one!")
            continue
        arr = list(board) #  changes to array to allow editing
        arr[idx] = side
        return "".join(arr) #  changes back to string
        

board = "_________"
draw_board(board)
nb_moves = 0
while True:
    if nb_moves % 2 == 0:
        board = move(board, "X")
    else:
        board = move(board, "O")
    nb_moves += 1
    draw_board(board)
    if evaluate(board): #  ends cicle if game is over
        break
