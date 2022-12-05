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

    # Rock Paper Scissor Definitions
    if player_2 == "X":
        counter += 1 # if its rock
    if player_2 == "Y":
        counter += 2 # if its paper
    if player_2 == "Z":
        counter += 3 # if its scissor

    # WIN LOSE DRAW, possibilities
    if player_2 == "X" and player_1 == "A":
        counter += 3 # draw
    if player_2 == "X" and player_1 == "B":
        counter += 0 # Lose
    if player_2 == "X" and player_1 == "C":
        counter += 6 # win

    if player_2 == "Y" and player_1 == "A":
        counter += 6 # win
    if player_2 == "Y" and player_1 == "B":
        counter += 3 # draw
    if player_2 == "Y" and player_1 == "C":
        counter += 0 # Lose

    if player_2 == "Z" and player_1 == "A":
        counter += 0 # Lose
    if player_2 == "Z" and player_1 == "B":
        counter += 6 # win
    if player_2 == "Z" and player_1 == "C":
        counter += 3 # draw

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
        counter += 3 # draw because of Y
        counter += 1 # Rock 1
    if player_2 == "Y" and player_1 == "B":
        counter += 3 # draw because of Y
        counter += 2 # Paper 2
    if player_2 == "Y" and player_1 == "C":
        counter += 3 # draw because of Y
        counter += 3 # Scissor 3

    # LOSE
    if player_2 == "X" and player_1 == "A":
        counter += 0 # lose because of X
        counter += 3 # Scissor 3
    if player_2 == "X" and player_1 == "B":
        counter += 0 # lose because of X
        counter += 1 # Rock 1
    if player_2 == "X" and player_1 == "C":
        counter += 0 # lose because of X
        counter += 2 # Paper 2

    #WIN
    if player_2 == "Z" and player_1 == "A":
        counter += 6 # win because of Z
        counter += 2 # Paper 2
    if player_2 == "Z" and player_1 == "B":
        counter += 6 # win because of Z
        counter += 3 # Scissor 3
    if player_2 == "Z" and player_1 == "C":
        counter += 6 # win because of Z
        counter += 1 # Rock 1

print(f"PART II {counter}")