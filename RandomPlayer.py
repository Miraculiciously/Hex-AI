import numpy as np

from Board import Board


class RandomPlayer:
    def __init__(self, color: str):
        self.own_color = color

    def get_move(self, board: Board):
        board.draw_boad()
        valid_moves = [n for n in range(0,board.N**2) if board.colors[n] == 'white']
        return np.random.choice(valid_moves)

if __name__ == "__main__":
    board = Board(4)
    random_player = RandomPlayer("red")
    random_player.get_move(board)