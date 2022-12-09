import string
import re
# Parsing
with open("day-7.in") as d:
    cmds = d.read().splitlines()

#print(cmds)
small_letters = list(string.ascii_uppercase)
cur_dir = "/"
all_dir = []

def new_list(cmds,index):
    new_list = [cmds[index].split(" ")[2]]
    cmds = cmds[index+1:]

    for line in cmds[index:]:
        #print(f"NEW LIST {cmds[index]}")

        if line.split(" ")[0][0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            #print(f"""new file added to new list {line.split(" ")[0]} bytes named {"".join(line.split(" ")[1:])}""")
            new_list.append(int(line.split(" ")[0]))
        elif line.split(" ")[1] == "ls":
            continue

        elif re.search("\$ cd [a-z]", line):
            #print("NOMMAAL")
            new_list_2 = [line.split(" ")[2]]
            for line_new in cmds[index+1:]:
                if line_new.split(" ") == "ls":
                    continue

                elif line_new.split(" ")[0][0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    #print(f"""new file added to new list 2 {line_new.split(" ")[0]} bytes named {"".join(line_new.split(" ")[1:])}""")
                    new_list_2.append(int(line_new.split(" ")[0]))


                elif line_new == "$ cd ..":
                    #print(f"NEW LIST 2 {new_list_2}")
                    new_list.append(new_list_2)

        elif line.split(" ")[1] == "..":
            break

    return new_list



liste_test = []
for index,line in enumerate(cmds):
    if line.split(" ")[1] == "ls":
        continue
        #print("show content")
    elif line.split(" ")[0] == "dir":
        continue

    elif line.split(" ")[1] == "cd":
        liste_test.append(new_list(cmds,index))

    else:
        liste_test.append((int(line.split(" ")[0])))

#print(liste_test[0:4])

def part_1(liste):
    root = 0
    ebene1 = []
    ebene2 = []
    more_100000 = []
    for index, x in enumerate(liste):
        if type(x) == int:
            root+= x
        if type(x) == list:
            ebene1.append(x)
    #print(root)

    for e1 in ebene1:
        e1_sum = []
        for e1_ in e1[1:]:
            if type(e1_) == int:
                e1_sum.append(int(e1_))
            if type(e1_) == list:
                ebene2.append(e1_)
        if sum(e1_sum) < 100000:
            more_100000.append(sum(e1_sum))

    for e2 in ebene2:
        e2_sum = []
        for e2_ in e2[1:]:
            if type(e2_) == int:
                e2_sum.append(int(e2_))
            if type(e2_) == list:
                ebene2.append(e2_)
        if sum(e2_sum) < 100000:
            more_100000.append(sum(e2_sum))


    #print(more_100000)
    return sum(set(more_100000))

print(part_1(liste_test))

