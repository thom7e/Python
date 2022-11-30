import networkx as nx
import matplotlib.pyplot as plt

with open("day-12.in") as file:
    x = file.read().strip().split("\n")

beginnings = []
endings = []
edges = []
for splitting in x:
    beginnings.append(splitting.split("-")[0])
    endings.append(splitting.split("-")[1])
    edges.append((splitting.split("-")[0],splitting.split("-")[1]))

#print(beginnings,endings)

#Draw Graph
G = nx.Graph()
G.add_nodes_from(set(beginnings))
G.add_nodes_from(set(endings))
G.add_edges_from(edges)

#print(G)
nx.draw_networkx(G)
#print(nx.shortest_path(G, "start","end"))
#G= nx.complete_graph(G)
paths = []
for path in nx.all_simple_paths(G, source="start", target="end"):
    paths.append(path)
    counter = 0
    for z in path:

        if z != z.lower():
            counter += 1
        if counter == 1:
            for path_ in nx.all_simple_paths(G, source=str(z), target="end"):
                paths.append(path_)



print(paths)
paths_ = []
for x in paths:
    paths_.append((x))

G = nx.DiGraph(G)

print(G.nodes)
for u in G.nodes:
    print(u)
for small in paths:
    for x in small:
        counter = 0
        if x == x.lower():
            counter += 1
        if counter == 1:
            #print(G.adj(str(x)))
            print(small)

def try_(G):
    roots = []
    leaves = []
    for node in G.nodes :
      if G.in_degree(node) == 0 : # it's a root
        roots.append(node)
      elif G.out_degree(node) == 0 : # it's a leaf
        leaves.append(node)

    for root in roots :
      for leaf in leaves :
        for path in nx.all_simple_paths(G, root, leaf) :
          print(path)

    nx.draw_networkx(G, pos=nx.circular_layout(G))
    plt.show()

#print(try_(G))