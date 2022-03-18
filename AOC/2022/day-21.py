#Player 1 starting position: 1
#Player 2 starting position: 10

import random
#def roll_the_dice():
#    return random.randint(0,100)
player1 = 0
player2 = 0
counter_player1 = 1
counter_player2 = 10
counter_dice = 0
dice = 1

while True:
    if dice == 101:
        dice = 1
    counter_player1 += dice
    #print(f"Player1 würfelt {dice}")
    dice += 1

    counter_dice += 1

    if dice == 101:
        dice = 1
    #print(dice)
    counter_player1 += dice
    #print(f"Player1 würfelt {dice}")
    dice+= 1
    counter_dice += 1
    if dice == 101:
        dice = 1
    #print(dice)
    counter_player1 += dice
    #print(f"Player1 würfelt {dice}")
    dice += 1
    counter_dice += 1

    #print(f"Player 1 steht auf space {counter_player1}")


    if counter_player1 == 10:
        player1 += 10
        counter_player1 = counter_player1
    else:
        if len(str(counter_player1)) > 1:
            if int(str(counter_player1)[-1]) == 0:
                counter_player1 = 10
            else:
                counter_player1 = int(str(counter_player1)[-1])
            player1 += counter_player1
        else:
            counter_player1 = counter_player1
            player1 += counter_player1

    #print(f"Player1 {counter_player1,player1}")

    if player1 >= 1000 or player2 >= 1000:
        print(player1,player2)
        print(counter_dice)
        print(f"Player 1 siegt !Ergebnis PART I {player2 * counter_dice}")
        break

    counter_player2 += dice
    #print(f"Player2 würfelt {dice}")
    dice += 1
    counter_dice += 1
    if dice == 101:
        dice = 1

    #print(dice)
    counter_player2 += dice
    #print(f"Player2 würfelt {dice}")
    dice += 1
    counter_dice += 1
    if dice == 101:
        dice = 1
    #print(dice)
    counter_player2 += dice
    #print(f"Player2 würfelt {dice}")
    dice += 1
    counter_dice += 1

    #print(dice)
    #print(f"Player 2 steht auf space {counter_player2}")
    if counter_player2 == 10:
        player2 += 10
    else:
        if len(str(counter_player2)) > 1:
            if int(str(counter_player2)[-1]) == 0:
                counter_player2 = 10
            else:
                counter_player2 = int(str(counter_player2)[-1])
            player2 += counter_player2
        else:
            counter_player2 = counter_player2
            player2 += counter_player2

    #print(f"Player2 {counter_player2,player2}")



    if player1 >= 1000 or player2 >= 1000:
        print(player1,player2)
        print(counter_dice)
        print(f"Player 2 siegt! Ergebnis PART I {player1*counter_dice}")
        break


