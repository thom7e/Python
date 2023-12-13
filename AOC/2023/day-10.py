def find_start(grid):
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == 'S':
                return x, y
    return None

def move(grid, current_position, previous_position):
    x, y = current_position
    px, py = previous_position

    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        direction = grid[y][x]
        if direction in "|-LJ7F":
            if direction == "|":
                return (x, y + 1) if y >= py else (x, y - 1)  # Unten, wenn von oben kommend, sonst oben
            elif direction == "-":
                return (x + 1, y) if x >= px else (x - 1, y)  # Rechts, wenn von links kommend, sonst links
            elif direction == "L":
                return (x + 1, y) if y > py else (x, y - 1)  # Rechts, wenn von oben kommend, sonst oben
            elif direction == "J":
                return (x - 1, y) if y > py else (x, y - 1)  # Links, wenn von oben kommend, sonst oben
            elif direction == "7":
                return (x - 1, y) if y < py else (x, y + 1)  # Links, wenn von unten kommend, sonst unten
            elif direction == "F":
                return (x + 1, y) if y < py else (x, y + 1)  # Rechts, wenn von unten kommend, sonst unten
    return None  # Keine Bewegung oder ungültiges Zeichen



def find_first_step(grid, start):
    x, y = start
    neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]  # Oben, Unten, Links, Rechts

    for nx, ny in neighbors:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] in "|-LJ7F":
            return nx, ny
    return None


def follow_path(grid, start):
    path = [start]
    previous_position = start

    while True:
        new_position = move(grid, path[-1], previous_position)
        if new_position and new_position != path[-1]:
            path.append(new_position)
            previous_position = path[-2]
        else:
            break  # Ende des Weges oder ungültiges Zeichen

    return path


def find_all_first_steps(grid, start):
    x, y = start
    neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]  # Oben, Unten, Links, Rechts
    first_steps = []

    for nx, ny in neighbors:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] in "|-LJ7F":
            first_steps.append((nx, ny))
    return first_steps


def read_grid_from_file(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append(line.strip())  # Entfernt Zeilenumbrüche am Ende jeder Zeile
    return grid

# Beispiel für das Lesen des Grids aus der Datei
grid = read_grid_from_file("day-10.in")

start_position = find_start(grid)
if start_position is None:
    print("Kein Startpunkt gefunden!")
else:
    all_first_steps = find_all_first_steps(grid, start_position)
    all_paths = []

    for first_step in all_first_steps:
        path = follow_path(grid, first_step)
        all_paths.append(path)

    # Finden des längsten Loops
    max_length = 0
    for path in all_paths:
        if len(path) > max_length:
            max_length = len(path)

    # Überprüfen, ob es mehrere Wege mit maximaler Länge gibt
    max_length_paths = [path for path in all_paths if len(path) == max_length]

    if max_length_paths:
        print(f"Längster Loop hat eine Länge von: {max_length // 2}")
        for i, path in enumerate(max_length_paths):
            print(f"Weg {i + 1} mit maximaler Länge: {len(path)}")
    else:
        print("Kein Loop gefunden")


