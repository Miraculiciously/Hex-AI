# holds game logic
import numpy as np

from Board import Board
from HumanPlayer import HumanPlayer

CONNECTED_VECTORS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1)]


class Game:
    """
    Class Game holds most of the game logic such as the win condition and is able to check whether a move is legal.
    """
    def __init__(self):
        self.board = Board(4)
        self.blue_player = HumanPlayer("blue")
        self.red_player = HumanPlayer("red")
        self.blue_player_turn = True

    def game_finished(self, player_color: int) -> bool:
        """
        Function to check if a certain player won the game
        :param player_color: red = 1, blue = 2, empty = 0
        :return:
        """
        # flood fill algorithm
        # Fip board if looking at the other player
        board_mat = self.board.board_state if player_color == 1 else self.board.board_state.T
        # Find cell of player_color on the first row
        to_explore = [(0, x[0]) for x in np.argwhere(board_mat[0] == player_color)]
        explored = set(to_explore)
        # Flood fill until you find a cell on the last row
        while to_explore:
            current_cell = to_explore.pop()
            for vector in CONNECTED_VECTORS:
                x, y = current_cell[0] + vector[0], current_cell[1] + vector[1]
                if 0 <= x < self.board.N and 0 <= y < self.board.N and (x, y) not in explored:
                    if board_mat[x, y] == player_color:
                        if x == self.board.N - 1:
                            return True
                        explored.add((x, y))
                        to_explore.append((x, y))
        return False

    def check_move(self, index, player) -> bool:
        # is this move legal
        return True

    def play_game(self):
        while not self.game_finished(1) and not self.game_finished(2):
            if self.blue_player_turn:
                x, y = self.blue_player.get_move(self.board)
                self.board.make_move(x, y, 2)
            else:
                x, y = self.red_player.get_move(self.board)
                self.board.make_move(x, y, 1)
            self.blue_player_turn = not self.blue_player_turn


if __name__ == '__main__':
    game = Game()
    game.play_game()

    # print(game.game_finished(2))
    # game.board.make_move(0, 0, 1)
    # game.board.make_move(0, 2, 2)
    # game.board.make_move(1, 2, 2)
    # game.board.make_move(2, 2, 2)
    # game.board.make_move(2, 2, 2)
    # game.board.make_move(3, 1, 2)
    # game.board.make_move(3, 0, 2)
    # game.board.make_move(1, 3, 2)
    # game.board.draw_boad()
    # print(game.game_finished(2))

