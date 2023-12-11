import re

def p1():
    with open("day-2.in", "r") as file:
        lines = file.read().splitlines()
        res = 0
        for id, line in enumerate(lines):
            possible = True
            # games = re.findall('\d+', line.split(':')[-1])
            games_red = re.findall('\d+ red', line.split(':')[-1])
            games_blue = re.findall('\d+ blue', line.split(':')[-1])
            games_green = re.findall('\d+ green', line.split(':')[-1])

            for game_red in games_red:

                if int(game_red.split(' ')[0]) > 12:

                    possible = False
            for game_green in games_green:

                if int(game_green.split(' ')[0]) > 13:
                    possible = False
            for game_blue in games_blue:

                if int(game_blue.split(' ')[0]) > 14:
                    possible = False

            if possible:
                res += id+1
    return res
print(f"p1 {p1()}")

def p2():
    with open("day-2.in", "r") as file:
        summe = 0
        lines = file.read().splitlines()
        res = 0
        for id, line in enumerate(lines):
            red = re.findall(r'\d+ red',line)
            blue = re.findall(r'\d+ blue',line)
            green = re.findall(r'\d+ green',line)
            score_red = max([int(x) for x in re.findall(r'\d+',str(red))])
            score_green = max([int(x) for x in re.findall(r'\d+',str(green))])
            score_blue = max([int(x) for x in re.findall(r'\d+',str(blue))])
            summe += int(score_red)*int(score_blue)*int(score_green)
            #print(f'Game {id+1}, red cubes {score_red}, blue cubes {score_blue} and green cubes {score_green}; SCORE: {int(score_red)*int(score_blue)*int(score_green)}')
    return summe

print(f"p2 {p2()}")
