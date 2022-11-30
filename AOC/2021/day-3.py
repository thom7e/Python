import re
from collections import Counter
import math
with open("day-3") as f:
    dir = f.read().split("\n")

check_count = []
gamma_rate = []
epsilon_rate = []
for x in range(len(dir[0])):
    for code in dir:
        for count, value in enumerate(code):
            if count == x:
                check_count.append(int(value))

    zero_counter= 0
    one_counter= 0
    for zero in check_count:
        if zero == 0:
            zero_counter += 1

        else:
            one_counter += 1

    if zero_counter > one_counter:
        gamma_rate.append(str(0))
        epsilon_rate.append(str(1))


    else:
        gamma_rate.append(str(1))
        epsilon_rate.append(str(0))


    check_count = []

gamma_bin = "".join(gamma_rate)
epsilon_bin = "".join(epsilon_rate)

print(f"Part 1: {int(gamma_bin,2)*int(epsilon_bin,2)}")

