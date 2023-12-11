# A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
from collections import Counter
with open("day-7.in") as f:
    file = f.read().splitlines()

def benutzerdefinierte_sortierung(value):
    ranking = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7, "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0}
    return ranking.get(value, -1)

def benutzerdefinierte_sortierung2(value):
    ranking = {"A": 12, "K": 11, "Q": 10, "T": 9, "9": 8, "8": 7, "7": 6, "6": 5, "5": 4, "4": 3, "3": 2,"2": 1, "J": 0}
    return ranking.get(value, -1)

def change_J(hand):
    hand = hand.replace("J",Counter(hand).most_common(1)[0][0])
    return hand



def get_total_winnings_(file):
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for hands in file:
        hand,bid = Counter(hands.split(" ")[0]), hands.split(" ")[1]
        #print(hands.split(" ")[0],hand.values(),len(hand.values()))
        if len(hand.values()) == 1:
            five_of_a_kind.append((hands.split(" ")[0],bid))
            # print("Five of a Kind", hand,hands)
        if len(hand.values()) == 2:
            if int(3) in hand.values() and int(2) in hand.values():
                full_house.append((hands.split(" ")[0], bid))
                # print("FULL HOUSE", hand,hands)
            elif int(4) in hand.values():
                four_of_a_kind.append((hands.split(" ")[0],bid))
                # print("Four of a Kind",hand,hands)
        elif len(hand.values()) == 3:
            if int(2) in hand.values() and not int(3) in hand.values():
                two_pair.append((hands.split(" ")[0], bid))
                # print("TWO PAIR",hand,hands)
            elif int(3) in hand.values() and not int(2) in hand.values():
                three_of_a_kind.append((hands.split(" ")[0], bid))
                # print("THREE OF A KIND", hand,hands)
        elif len(hand.values()) == 4:
            one_pair.append((hands.split(" ")[0], bid))
            # print("ONE PAIR", hand,hands)
        elif len(hand.values()) == 5:
            high_card.append((hands.split(" ")[0], bid))
            # print("HIGH CARD", hand,hands)
    print(one_pair)

    # FIVE OF A KIND
    foak_sorted = sorted(five_of_a_kind, key=lambda x: [benutzerdefinierte_sortierung(c) for c in x[0]], reverse=True)
    #print("sorted five of a kind",foak_sorted)
    # FOUR OF A KIND
    fouak_sorted = sorted(four_of_a_kind, key=lambda x: [benutzerdefinierte_sortierung(c) for c in x[0]], reverse=True)
    #print("sorted four of a kind",fouak_sorted)
    # FULL HOUSE
    fuho_sorted = sorted(full_house, key=lambda x: [benutzerdefinierte_sortierung(c) for c in x[0]], reverse=True)
    #print("sorted full house",fuho_sorted)
    # THREE OF A KIND
    toak_sorted = sorted(three_of_a_kind, key=lambda x: [benutzerdefinierte_sortierung(c) for c in x[0]], reverse=True)
    # print("sorted three of a kind",toak_sorted)
    tp_sorted = sorted(two_pair, key=lambda x: [benutzerdefinierte_sortierung(c) for c in x[0]], reverse=True)
    # print("sorted two pair",tp_sorted)
    op_sorted = sorted(one_pair, key=lambda x: [benutzerdefinierte_sortierung(c) for c in x[0]], reverse=True)
    # print("sorted one pair",op_sorted)
    hp_sorted = sorted(high_card, key=lambda x: [benutzerdefinierte_sortierung(c) for c in x[0]], reverse=True)
    # print("sorted high card",hp_sorted)

    reihenfolge = foak_sorted+fouak_sorted+fuho_sorted+toak_sorted+tp_sorted+op_sorted+hp_sorted

    summe = 0
    for index, bid in enumerate(reversed(reihenfolge)):
        summe += ((index+1) * int(bid[1]))

    return summe
print("p1", get_total_winnings_(file))

def get_total_winnings_p2(file):
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    one_pair = []
    high_card = []

    for hands in file:
        hand = change_J(hands.split(" ")[0])
        hand,bid = Counter(hand), hands.split(" ")[1]

        #print(hands.split(" ")[0],hand.values(),len(hand.values()))
        if len(hand.values()) == 1:
            if (change_J(hands.split(" ")[0]),bid) in five_of_a_kind:
                if (change_J(hands.split(" ")[0]),bid) == (hands.split(" ")[0],bid):
                    print("original")
                else:
                    print("changed")

            # print("Five of a Kind", hand,hands)
        if len(hand.values()) == 2:
            if int(3) in hand.values() and int(2) in hand.values():
                full_house.append((change_J(hands.split(" ")[0]), bid))
                # print("FULL HOUSE", hand,hands)
            elif int(4) in hand.values():
                four_of_a_kind.append((change_J(hands.split(" ")[0]),bid))
                # print("Four of a Kind",hand,hands)
        elif len(hand.values()) == 3:
            if int(2) in hand.values() and not int(3) in hand.values():
                two_pair.append((change_J(hands.split(" ")[0]), bid))
                # print("TWO PAIR",hand,hands)
            elif int(3) in hand.values() and not int(2) in hand.values():
                three_of_a_kind.append((change_J(hands.split(" ")[0]), bid))
                # print("THREE OF A KIND", hand,hands)
        elif len(hand.values()) == 4:
            one_pair.append((change_J(hands.split(" ")[0]), bid))
            # print("ONE PAIR", hand,hands)
        elif len(hand.values()) == 5:
            high_card.append((change_J(hands.split(" ")[0]), bid))
            # print("HIGH CARD", hand,hands)
    print(one_pair)

    # FIVE OF A KIND
    foak_sorted = sorted(five_of_a_kind, key=lambda x: [benutzerdefinierte_sortierung2(c) for c in x[0]], reverse=True)
    #print("sorted five of a kind",foak_sorted)
    # FOUR OF A KIND
    fouak_sorted = sorted(four_of_a_kind, key=lambda x: [benutzerdefinierte_sortierung2(c) for c in x[0]], reverse=True)
    #print("sorted four of a kind",fouak_sorted)
    # FULL HOUSE
    fuho_sorted = sorted(full_house, key=lambda x: [benutzerdefinierte_sortierung2(c) for c in x[0]], reverse=True)
    #print("sorted full house",fuho_sorted)
    # THREE OF A KIND
    toak_sorted = sorted(three_of_a_kind, key=lambda x: [benutzerdefinierte_sortierung2(c) for c in x[0]], reverse=True)
    # print("sorted three of a kind",toak_sorted)
    tp_sorted = sorted(two_pair, key=lambda x: [benutzerdefinierte_sortierung2(c) for c in x[0]], reverse=True)
    # print("sorted two pair",tp_sorted)
    op_sorted = sorted(one_pair, key=lambda x: [benutzerdefinierte_sortierung2(c) for c in x[0]], reverse=True)
    # print("sorted one pair",op_sorted)
    hp_sorted = sorted(high_card, key=lambda x: [benutzerdefinierte_sortierung2(c) for c in x[0]], reverse=True)
    # print("sorted high card",hp_sorted)

    reihenfolge = foak_sorted+fouak_sorted+fuho_sorted+toak_sorted+tp_sorted+op_sorted+hp_sorted
    print(reihenfolge)
    summe = 0
    for index, bid in enumerate(reversed(reihenfolge)):
        summe += ((index+1) * int(bid[1]))

    return summe

print(get_total_winnings_p2(file))
# beispielliste = [('8939K', '547'), ('47TJ4', '431'), ('9Q75Q', '826'), ('Q266J', '278'), ('682J6', '385'), ('657A5', '540'), ('34KA4', '891')]
# sorted_beispielliste = sorted(beispielliste, key=lambda x: [benutzerdefinierte_sortierung(c) for c in x[0]], reverse=True)
# print(sorted_beispielliste)