import itertools
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


class Board:
    def __init__(self, N=11):
        self.game_network = np.zeros((N ** 2, N ** 2))
        for i in range(0, N ** 2 - 1):
            if i % N != N - 1:
                self.game_network[i, i + 1] = 1
                self.game_network[i + 1, i] = 1
            if i < N ** 2 - N:
                self.game_network[i, N + i] = 1
                self.game_network[N + i, i] = 1
                if i % N != N - 1:
                    self.game_network[i + 1, N + i] = 1
                    self.game_network[N + i, i + 1] = 1
        self.G = nx.from_numpy_matrix(self.game_network)
        self.colors = ['white' for n in self.G.nodes]
        self.red_side = itertools.product(np.arange(0, N), np.arange(N ** 2 - N, N ** 2))
        self.blue_side = itertools.product(np.arange(0, N ** 2 - N + 1, N), np.arange(N - 1, N ** 2, N))

    def draw_boad(self) -> None:
        nx.draw(self.G, with_labels=True, node_color=self.colors)
        plt.show()

    def make_move(self, index, color):
        self.colors[index] = color


if __name__ == '__main__':
    board = Board(4)
    board.draw_boad()
    board.make_move(1, "red")
    board.make_move(0, "red")
    board.make_move(5, "red")
    board.make_move(9, "red")
    board.make_move(13, "red")
    board.make_move(14, "red")
    board.draw_boad()