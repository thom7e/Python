import numpy as np

with open("day-9.in") as d:
    inp = d.read().splitlines()

def adjust(head,tail):
    check_x = (head[0]-tail[0])
    check_y = (head[1]-tail[1])
    if abs(check_x)<=1 and abs(check_y)<=1:
        # ok
        pass
    elif abs(check_x)>=2 and abs(check_y)>=2:
        #2       2       2
        # 1   ->  1   ->  .   -> 2
        #  head       .head      1head     1head
        tail = (head[0]-1 if tail[0]<head[0] else head[0]+1, head[1]-1 if tail[1]<head[1] else head[1]+1)
    elif abs(check_x)>=2:
        # tail     tail       .
        #  head ->  .head  ->  tailhead
        tail = (head[0]-1 if tail[0]<head[0] else head[0]+1, head[1])
    elif abs(check_y)>=2:
        tail = (head[0], head[1]-1 if tail[1]<head[1] else head[1]+1)
    return tail

head = (0,0)
tail = [(0,0) for _ in range(9)]
DR = {'L': 0, 'U': -1, 'R': 0, 'D': 1}
DC = {'L': -1, 'U': 0, 'R': 1, 'D': 0}
part_1 = [tail[0]]
part_2 = [tail[8]]
for line in inp:
    dir,amount = line.split()
    amount = int(amount)
    for _ in range(amount):
        head = (head[0] + DR[dir], head[1]+DC[dir])
        tail[0] = adjust(head, tail[0])
        for i in range(1, 9):
            tail[i] = adjust(tail[i-1], tail[i])
        part_1.append(tail[0])
        part_2.append(tail[8])
print("PART I: ",len(set(part_1)))
print("PART II: ",len(set(part_2)))