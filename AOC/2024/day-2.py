import re

with open("day-2.in") as input:
    inp = input.read().splitlines()


def increasing_or_decreasing(lst, max_step=3):

    is_increasing = all(0 < lst[i + 1] - lst[i] <= max_step for i in range(len(lst) - 1))
    is_decreasing = all(0 < lst[i] - lst[i + 1] <= max_step for i in range(len(lst) - 1))

    return is_increasing or is_decreasing


def increasing_or_decreasing_eventuell(lst, max_step=3):
    if increasing_or_decreasing(lst, max_step):
        return True  # Die Liste erfüllt bereits die Bedingung
    # Prüfe, ob die Bedingung erfüllt wird, wenn ein Element entfernt wird
    for i in range(len(lst)):
        temp_lst = lst[:i] + lst[i + 1:]  # Entferne das i-te Element
        if increasing_or_decreasing(temp_lst, max_step):
            return True

    return False  # Bedingung kann nicht erfüllt werden

counter_p1 = 0
for liste in inp:
    dec_o = liste.split(" ")
    dec= [int(x) for x in dec_o]
    if increasing_or_decreasing(dec):
        counter_p1 += 1

counter_p2 = 0
for liste in inp:
    dec_o = liste.split(" ")
    dec= [int(x) for x in dec_o]
    if increasing_or_decreasing_eventuell(dec):
        counter_p2 += 1

print(f"Part I: {counter_p1}")
print(f"Part II: {counter_p2}")


