with open("day-4.in") as input:
    inp = input.readlines()

def p1(inp):
    score = 0
    for line in inp:
        winning_numbers, my_numbers = line.split("|")[0].split(":")[1], line.split("|")[1]
        w_n_list = [int(x) for x in winning_numbers.split(" ") if x != ""]
        my_n_list = [int(x) for x in my_numbers.split(" ") if x != ""]
        matches = set(w_n_list).intersection(set(my_n_list))
        points = 0
        if matches:
            points = 1
            for _ in range(1, len(matches)):
                points *= 2
        score += points

    return score


print(f"p1: {p1(inp)}")


def p2(inp):
    # Gesamtanzahl der Karten
    total_cards = len(inp)
    # Initialisiere eine Liste, die die Anzahl jeder Karte darstellt (zunächst 1 für jede Karte)
    gesamtkarten = [1] * total_cards

    for index, line in enumerate(inp):
        # Trenne die Gewinnzahlen und Ihre Zahlen in der Karte
        winning_numbers, my_numbers = line.split("|")[0].split(":")[1], line.split("|")[1]
        w_n_list = [int(x) for x in winning_numbers.split(" ") if x != ""]
        my_n_list = [int(x) for x in my_numbers.split(" ") if x != ""]
        matches = len(set(w_n_list).intersection(set(my_n_list)))

        # Für jede Übereinstimmung, füge die entsprechende Anzahl an zusätzlichen Karten hinzu
        for i in range(1, matches + 1):
            next_card_index = index + i
            # Stelle sicher, dass der Index der nächsten Karte im gültigen Bereich liegt
            if next_card_index < total_cards:
                gesamtkarten[next_card_index] += gesamtkarten[index]

    # Berechne die Gesamtanzahl der Karten, einschließlich der gewonnenen Karten
    return sum(gesamtkarten)



print(f"p2: {p2(inp)}")
