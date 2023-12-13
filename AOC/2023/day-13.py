import numpy as np

def read_grids_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    # Trenne die verschiedenen Grids an den Leerzeilen
    raw_grids = content.strip().split('\n\n')

    # Konvertiere jedes Grid in ein Numpy-Array
    grids = [np.array([list(line) for line in grid.split('\n')]) for grid in raw_grids]

    return grids


def check_fold(grid):
    rows, cols = grid.shape

    # Überprüfe jede Spalte
    for col in range(1, cols):
        if col <= cols // 2:
            left = grid[:, :col]
            right = np.fliplr(grid[:, col:2*col])
        else:
            right = np.fliplr(grid[:, col:])
            left = grid[:, 2*col-cols:col]

        if left.shape == right.shape and np.array_equal(left, right):
            #print("spalte", col)
            return ("col",col)

    # Überprüfe jede Zeile
    for row in range(1, rows):
        if row <= rows // 2:
            top = grid[:row, :]
            bottom = np.flipud(grid[row:2*row, :])
        else:
            bottom = np.flipud(grid[row:, :])
            top = grid[2*row-rows:row, :]

        if top.shape == bottom.shape and np.array_equal(top, bottom):
            #print("reihe",row)
            return ("row",int(row*100))

    return 0


def check_fold_p2(grid,oldgrid):
    rows, cols = grid.shape

    # Überprüfe jede Spalte
    for col in range(1, cols):
        if col <= cols // 2:
            left = grid[:, :col]
            right = np.fliplr(grid[:, col:2*col])
        else:
            right = np.fliplr(grid[:, col:])
            left = grid[:, 2*col-cols:col]

        if left.shape == right.shape and np.array_equal(left, right):
            if not check_fold(oldgrid) == ("col",col):
                return ("col",col)

    # Überprüfe jede Zeile
    for row in range(1, rows):
        if row <= rows // 2:
            top = grid[:row, :]
            bottom = np.flipud(grid[row:2*row, :])
        else:
            bottom = np.flipud(grid[row:, :])
            top = grid[2*row-rows:row, :]

        if top.shape == bottom.shape and np.array_equal(top, bottom):

            if check_fold(oldgrid) == ("row", int(row*100)):

                continue
            return ("row", row*100)

def modify_grids(grid):
    rows, cols = grid.shape
    for row in range(rows):
        for col in range(cols):
            modified_grid = grid.copy()
            modified_grid[row, col] = '#' if grid[row, col] == '.' else '.'
            modified_fold_result = check_fold_p2(modified_grid,grid)
            if check_fold_p2(modified_grid,grid):
                return modified_fold_result



# Beispiel: Verwenden der Funktion auf den Grids aus der Datei
grids = read_grids_from_file("day-13.in")
summe = 0
for i, grid in enumerate(grids):
    result = check_fold(grid)[1]
    summe += result
    #print(f"Grid {i+1}: {result}")

print("p1",summe)

summe_p2 = 0

for grid in grids:
    result_p2 = modify_grids(grid)[1]
    summe_p2 += result_p2
print("p2",summe_p2)
