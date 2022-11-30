import numpy as np
with open("day-20.in") as file:
    f = file.read().strip().split("\n")

output = "##..##...#...##.##...##.##..####....##...##.#.######....###.##...##.##....#..#..###..##.##.###.#..##.###.#......##.#####..#...#...#.#.....#.###.#..#######....##.##.#.#.....##.#.##...#...###.####.#.#####...#..#..#######....#..##.....##.##.#####.####.....#...##..#..#.###....#..##.#....##.##..###...##.##.##.####....##.#...#.#.#.###########...###.###.#.#.###..##.######...#..#.##.......##.#.###....#..##....#.#..##..##..###.#...#.##.#..##..##..####.#.##.#.....###.#..####....#..##...##.##..###...#...#..##..#.#..#."


G = np.empty(shape=(len(f),len(f[0])),dtype=str)
for x in range(len(f)):
    for y in range(len(f[1])):
        G[x][y] = str(f[x][y])

G_output = G.copy()
def beispiel(G,output,x_in,y_in):
    roundaround = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]
    #G_new = G.copy()
    binary = str()

    for x,y in roundaround:
        try:
            if G[x_in+x][y+y_in] == "#":
                binary += str(1)
            elif G[x+x_in][y+y_in] == ".":
                binary += str(0)
        except IndexError:
            binary += str(0)
        #G_new[x_in][y_in] = output[int(binary,2)]
    return output[int(binary,2)]

for x in range(len(G)):
    for y in range(len(G[0])):
        G_output[x][y] = beispiel(G,output,x,y)

print(G_output)
G = G_output.copy()

for i in range(len(G)):
    for j in range(len(G[0])):
        G_output[i][j] = beispiel(G,output,i,j)

print(G_output)

counter = 0
for a in range(len(G_output)):
    for b in range(len(G_output[0])):
        if G_output[a][b] == "#":
            counter += 1
print(counter)

