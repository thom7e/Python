import numpy as np


def detect_row(board) -> bool:
    """Check if the board has one complete row"""
    for j in range(5):
        row = board[j, :]
        if (not 0 in row):
            return True
    return False


def detect_column(board) -> bool:
    """Check if the board has one complete column"""
    for i in range(5):
        column = board[:, i]
        if (not 0 in column):
            return True
    return False


def get_winning_board(boards) -> int:
    """Check if a board is winning (at least one complete row or column)"""
    for i in range(len(boards)):
        if (detect_row(boards[i]) or detect_column(boards[i])):
            return i
    return -1


def calculate_board_score(board, marked_board) -> int:
    """Calculate the board score using the remaining values"""
    buffer = board.copy()
    for j in range(board.shape[0]):
        for i in range(board.shape[1]):
            if (marked_board[j, i] == 1):
                buffer[j, i] = 0
    return buffer.sum()


def get_bingo_sequence():
    """Read the first line from the input file"""
    with open("day-4.in", "r") as file:
        sequence = file.readline()
    sequence = sequence.rstrip().split(",")
    sequence = [int(i) for i in sequence]
    return sequence


sequence = get_bingo_sequence()

with open("day-4.in", "r") as file:
    x = file.readlines()

# Remove the first line (bingo sequence)
inline_grids = x[x.index("\n")::]

# Remove all line break for each row of all boards
for i, r in enumerate(inline_grids):
    r = r.replace("\n", "")
    inline_grids[i] = r

boards = []
grid = []

# Transform each board rows from list of strings into numpy matrix (2D grid)
for r in inline_grids:
    if (r == ""):
        boards.append(np.matrix(grid, int))
        grid = []
    else:
        row = [int(i) for i in r.split()]
        grid.append(row)

# Remove empty boards
boards.remove(boards[0])
for g in boards:
    if (len(g) == 0):
        boards.remove(g)

# Create marked down boards corresponding to each bingo boards
marked_boards = []
shape = (5, 5)
for i in range(len(boards)):
    marked_boards.append(np.zeros(shape, int))

# Complete all bingo boards with given number from the game's sequence
for n in sequence:
    for i in range(len(boards)):
        if (n in boards[i]):
            y, x = np.where(boards[i] == n)
            if (len(y) == 0 and len(x) == 0):
                continue
            # Put a one to mark down a number in the board
            marked_boards[i][y, x] = 1

    # Catch the first winning board and calculate the score of this board
    winning_board_index = get_winning_board(marked_boards)
    if (winning_board_index != -1):
        score = calculate_board_score(
            boards[winning_board_index],
            marked_boards[winning_board_index]
        )
        print(n * score)
        break