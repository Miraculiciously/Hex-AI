import numpy as np
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import tensorflow as tf
import itertools

N = 4

game_network = np.zeros((N**2, N**2))

for i in range(0, N**2 - 1):
    if i % N != N - 1:
        game_network[i, i + 1] = 1
        game_network[i + 1, i] = 1
    if i < N**2 - N:
        game_network[i, N + i] = 1
        game_network[N + i, i] = 1
        if i % N != N - 1:
            game_network[i + 1, N + i] = 1
            game_network[N + i, i + 1] = 1

#print("Successfully created matrix of dim %i x %i." % (N, N))

G = nx.from_numpy_matrix(game_network)

colours = ['white' for n in G.nodes]




colours[1] = "red"
colours[2] = "red"
colours[5] = "red"
colours[9] = "red"
colours[13] = "red"
colours[14] = "red"

nx.draw(G, with_labels=True, node_color = colours)
plt.show()


red_side = itertools.product(np.arange(0,N), np.arange(N**2 - N, N**2))
blue_side = itertools.product(np.arange(0, N**2 - N + 1, N), np.arange(N-1, N**2, N))

player_colour = "red" # or "blue"
# AI magically chooses a x and y coordinate, x, y in [0, N - 1]
# colours[y*N + x] = player_colour

isolated = G.subgraph([n for n in G.nodes if colours[n] == player_colour])


if player_colour == "red":
    if any( [nx.has_path(isolated, x, y) for (x, y) in red_side if (x in isolated and y in isolated.nodes) ] ):
        print(player_colour, "wins!")
        # game ends etc.
else:
    if any( [nx.has_path(isolated, x, y) for (x, y) in blue_side if (x in isolated and y in isolated.nodes) ] ):
        print(player_colour, "wins!")
        # game ends etc.
