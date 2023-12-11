with open("day-8.in") as d:
    inp = d.read().splitlines()


dict_output = {}
for line in inp:
    key, value = line.split('=')
    # Entfernen von Leerzeichen und Klammern, Umwandlung in Tuple
    value = tuple(v.strip() for v in value.strip()[1:-1].split(','))
    dict_output[key.strip()] = value

def p1():
    start = "AAA"
    instructions = ("LRLRRRLRRRLLLRLRRLLRLRRRLRLRRRLRLRRRLRLRRRLRRRLRLLRRRLRLRLRRLRRLRLRRLRRLRRLLRRRLRRRLRRLRRLRRLRRRLLRRLRLRRLRLRRLRRLRLRRLRRLLRLRRRLRRLRRRLLRLRLRLLRLLRLLRLRRLLRRLRLRLRRLRLLRRRLLRRRLRRLLRRRLRRRLRLRRRLLRRRLRLRRRLLLRRRLRLRLRRRLRRRLRRRLRLRRLLLRRLRRRLLRLRRRLRLRLLLRRLRLRRRLRLRRRR")
    counter = 0
    while start != "ZZZ":
        for ins in instructions:
            if ins == "L":
                next_step = dict_output[start][0]
                #print("next step", next_step)
                start = next_step
                counter += 1
            else:
                next_step = dict_output[start][1]
                #print("next step", next_step)
                start = next_step
                counter += 1

            if start == "ZZZ":
                return counter

#print(p1())

def p2():
    starts = [x for x in dict_output.keys() if x[-1] == "A"]
    print("Startpunkte:", starts)
    instructions = ("LRLRRRLRRRLLLRLRRLLRLRRRLRLRRRLRLRRRLRLRRRLRRRLRLLRRRLRLRLRRLRRLRLRRLRRLRRLLRRRLRRRLRRLRRLRRLRRRLLRRLRLRRLRLRRLRRLRLRRLRRLLRLRRRLRRLRRRLLRLRLRLLRLLRLLRLRRLLRRLRLRLRRLRLLRRRLLRRRLRRLLRRRLRRRLRLRRRLLRRRLRLRRRLLLRRRLRLRLRRRLRRRLRRRLRLRRLLLRRLRRRLLRLRRRLRLRLLLRRLRLRRRLRLRRRR")

    current_positions = starts.copy()
    steps = 0

    while True:
        new_positions = []
        all_end_with_z = True  # Annahme, dass alle Positionen mit Z enden, bis das Gegenteil festgestellt wird

        for position in current_positions:
            if not position.endswith("Z"):
                all_end_with_z = False  # Mindestens eine Position endet nicht mit Z

            ins = instructions[steps % -len(instructions)]  # Aktuelle Anweisung

            if ins == "L":
                next_step = dict_output[position][0]
            else:
                next_step = dict_output[position][1]

            #print(f"Nächster Schritt für {position}: {next_step}")
            new_positions.append(next_step)  # Aktualisieren der neuen Position

        if all_end_with_z:
            print(f"Ziel erreicht nach {steps} Schritten.")
            return steps  # Beendet die Funktion, wenn alle Positionen mit Z enden

        steps += 1
        current_positions = new_positions  # Aktualisieren der Positionen für den nächsten Durchgang

# Stellen Sie sicher, dass dict_output korrekt definiert ist, bevor Sie diese Funktion aufrufen




print(p2())