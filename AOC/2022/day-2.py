with open("day-2.in") as f:
    rpc = f.read().splitlines()

# rock 1
# paper 2
# scissor 3

# win 6
# draw 3
# lose 0

# A und X Rock
# B und Y Paper
# C und Z Scissor

counter = 0
for play in rpc:
    player_1 = play.split(" ")[0]
    player_2 = play.split(" ")[1]

    # RPC
    if player_2 == "X":
        counter += 1
    if player_2 == "Y":
        counter += 2
    if player_2 == "Z":
        counter += 3

    # WIN LOSE DRAW
    if player_2 == "X" and player_1 == "A":
        counter += 3
    if player_2 == "X" and player_1 == "B":
        counter += 0
    if player_2 == "X" and player_1 == "C":
        counter += 6

    if player_2 == "Y" and player_1 == "A":
        counter += 6
    if player_2 == "Y" and player_1 == "B":
        counter += 3
    if player_2 == "Y" and player_1 == "C":
        counter += 0

    if player_2 == "Z" and player_1 == "A":
        counter += 0
    if player_2 == "Z" and player_1 == "B":
        counter += 6
    if player_2 == "Z" and player_1 == "C":
        counter += 3

print(f" PART I {counter}")

## PART II

# X = lose
# Y = draw
# Z = win

# rock 1
# paper 2
# scissor 3

# win 6
# draw 3
# lose 0

# A Rock
# B Paper
# C Scissor

counter = 0
for play in rpc:
    player_1 = play.split(" ")[0]
    player_2 = play.split(" ")[1]

    # DRAW
    if player_2 == "Y" and player_1 == "A":
        counter += 3
        counter += 1
    if player_2 == "Y" and player_1 == "B":
        counter += 3
        counter += 2
    if player_2 == "Y" and player_1 == "C":
        counter += 3
        counter += 3

    # LOSE
    if player_2 == "X" and player_1 == "A":
        counter += 0
        counter += 3
    if player_2 == "X" and player_1 == "B":
        counter += 0
        counter += 1
    if player_2 == "X" and player_1 == "C":
        counter += 0
        counter += 2

    #WIN
    if player_2 == "Z" and player_1 == "A":
        counter += 6
        counter += 2
    if player_2 == "Z" and player_1 == "B":
        counter += 6
        counter += 3
    if player_2 == "Z" and player_1 == "C":
        counter += 6
        counter += 1

print(f"PART II {counter}")