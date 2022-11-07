# light red bags contain 1 shiny gold bag, 2 muted yellow bags.
# dark orange bags contain 3 shiny gold bags, 4 muted yellow bags.
# shiny gold bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.

import re

with open("day7") as f:
    lines = f.readlines()

graph = {}

for i in lines:
    regex = re.match('(.+?) bags', i)
    color_primary = regex.group(1)
    color_inside = re.findall('(\d+) (.+?) bag', i)
    if len(color_inside) > 0:
        color_inside = color_inside
        graph[color_primary] = color_inside
        # print(color_inside)
    else:
        graph[color_primary] = [('0', '')]

print(graph)

def shiny_gold(color):
    if color == "shiny gold":
        return True
    elif color == "":
        return False
    else:
        return any(shiny_gold(child) for amount, child in graph[color])


print("part 1: ", sum(shiny_gold(color) for color in graph.keys()) - 1)


def count(color):
    if color == "":
        return 1
    return 1 + sum(int(amount) * count(child) for amount, child in graph[color])


print(count("shiny gold") - 1)
