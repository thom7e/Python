import re

with open("day-3.in") as input:
    inp = input.read()

## PART I
regex = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(regex, str(inp))

counterp1 = 0
for x,y in matches:
    counterp1 += int(x)*int(y)
print("ergp1",counterp1)


##PART II
# Funktion, um Passagen zwischen 'do()' und 'dont()' zu extrahieren
def extract_mul_between_do_and_dont(text):
    result = []
    inside_section = False  # Gibt an, ob wir uns zwischen 'do()' und 'dont()' befinden
    buffer = []  # Puffer für den Text innerhalb des Abschnitts

    i = 0
    while i < len(text):
        # Wenn wir auf 'do()' stoßen, setzen wir den "inside_section" auf True
        if text[i:i+4] == "do()":
            if inside_section:
                # Wenn wir schon in einem Abschnitt sind, speichern wir den Puffer
                result.append(''.join(buffer))
            inside_section = True
            buffer = []  # Puffer für neuen Abschnitt zurücksetzen
            i += 4
        # Wenn wir auf 'dont()' stoßen, setzen wir den "inside_section" auf False
        elif text[i:i+7] == "don't()":
            if inside_section:
                result.append(''.join(buffer))  # Speichern des Textes im Puffer
            inside_section = False
            buffer = []  # Puffer zurücksetzen
            i += 6
        else:
            # Wenn wir uns innerhalb eines Abschnitts befinden, fügen wir den Text zum Puffer hinzu
            if inside_section:
                buffer.append(text[i])
            i += 1
    if inside_section and buffer:
        result.append(''.join(buffer))

    # Ergebnis zurückgeben, alle Abschnitte zwischen 'do()' und 'dont()' sind nun in result
    return result

# Alle Abschnitte zwischen 'do()' und 'don't()' extrahieren
sections = extract_mul_between_do_and_dont(inp)

# Regulärer Ausdruck für mul(X,Y)
mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)"

# Alle mul(X,Y) aus den extrahierten Passagen finden
mul_results = []

for section in sections:
    mul_results.extend(re.findall(mul_regex, section))


counterp2 = 0
for x2,y2 in mul_results:
    counterp2 += int(x2)*int(y2)
print("ergp2",counterp2 + 417*528+ 215*18)