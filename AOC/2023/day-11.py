def read_grid_from_file(filename):
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            grid.append(line.strip())  # Entfernt Zeilenumbrüche am Ende jeder Zeile
    return grid

# Beispiel für das Lesen des Grids aus der Datei
grid = read_grid_from_file("day-11.in")

def ergaenze_grid_und_speichere_leere(grid):
    n_rows = len(grid)
    n_cols = len(grid[0])
    leere_spalten = []
    leere_zeilen = []

    # Identifiziere leere Spalten und Zeilen
    for col in range(n_cols):
        if all(grid[row][col] == '.' for row in range(n_rows)):
            leere_spalten.append(col)

    for row in range(n_rows):
        if all(char == '.' for char in grid[row]):
            leere_zeilen.append(row)

    # Ergänze leere Spalten
    erweitertes_grid = ['' for _ in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            if col in leere_spalten:
                erweitertes_grid[row] += '.'
            erweitertes_grid[row] += grid[row][col]

    # Ergänze leere Zeilen
    endgueltiges_grid = []
    for row in range(n_rows):
        if row in leere_zeilen:
            endgueltiges_grid.append('.' * len(erweitertes_grid[0]))
        endgueltiges_grid.append(erweitertes_grid[row])

    return endgueltiges_grid, leere_zeilen, leere_spalten

# Anwendung der erweiterten Methode
ergaenztes_grid, gespeicherte_leere_zeilen, gespeicherte_leere_spalten = ergaenze_grid_und_speichere_leere(grid)



def finde_koordinaten_von_hashtags(grid):
    koordinaten = []

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '#':
                koordinaten.append((row, col))

    return koordinaten


koordinaten_von_hashtags = finde_koordinaten_von_hashtags(grid)


def manhattan_distanz_mit_ergaenzung(punkt1, punkt2, ergaenzte_zeilen, ergaenzte_spalten,multi):
    # Berechne die grundlegende Manhattan-Distanz
    distanz = abs(punkt1[0] - punkt2[0]) + abs(punkt1[1] - punkt2[1])

    # Zähle die ergänzten Zeilen zwischen den beiden Punkten
    for zeile in ergaenzte_zeilen:
        if punkt1[0] < zeile < punkt2[0] or punkt2[0] < zeile < punkt1[0]:
            distanz += multi-1

    # Zähle die ergänzten Spalten zwischen den beiden Punkten
    for spalte in ergaenzte_spalten:
        if punkt1[1] < spalte < punkt2[1] or punkt2[1] < spalte < punkt1[1]:
            distanz += multi-1

    return distanz

def summe_aller_manhattan_distanzen_mit_ergaenzung(koordinaten, ergaenzte_zeilen, ergaenzte_spalten,multi):
    summe = 0
    for i in range(len(koordinaten)):
        for j in range(i + 1, len(koordinaten)):
            summe += manhattan_distanz_mit_ergaenzung(koordinaten[i], koordinaten[j], ergaenzte_zeilen, ergaenzte_spalten,multi)
    return summe

# Faktor p1
faktor = 2
gesamtsumme = summe_aller_manhattan_distanzen_mit_ergaenzung(koordinaten_von_hashtags,gespeicherte_leere_zeilen, gespeicherte_leere_spalten,faktor)
print("Summe aller Manhattan-Distanzen p1:", gesamtsumme)
# Faktor p2
faktor = 10**6
gesamtsumme = summe_aller_manhattan_distanzen_mit_ergaenzung(koordinaten_von_hashtags,gespeicherte_leere_zeilen, gespeicherte_leere_spalten,faktor)
print("Summe aller Manhattan-Distanzen p2:", gesamtsumme)