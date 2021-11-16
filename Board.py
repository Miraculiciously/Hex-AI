import numpy as np
import matplotlib.pyplot as plt


class Board:
    def __init__(self, N=11):
        self.N = N
        self.board_state = np.zeros((N, N))

    def draw_boad(self) -> None:
        plt.matshow(self.board_state)
        plt.show()

    def make_move(self, x, y, color):
        self.board_state[x, y] = color

    # def make_move(self, index, color):
    #     x = index % self.N
    #     y = index // self.N
    #     self.make_move(x, y, color)


if __name__ == '__main__':
    board = Board(4)
    board.draw_boad()
    board.make_move(0, 0, 1)
    board.make_move(0, 1, 2)
    board.draw_boad()
