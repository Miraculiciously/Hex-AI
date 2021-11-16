import numpy as np

from Board import Board


class RandomPlayer:
    def __init__(self, color: int):
        self.own_color = color

    def get_move(self, board: Board):
        rng = np.random.default_rng()
        valid_moves = np.argwhere(board.board_state == 0)
        return rng.choice(valid_moves, 1, axis=0)[0]


if __name__ == "__main__":
    board = Board(4)
    random_player = RandomPlayer(1)
    print(random_player.get_move(board))
