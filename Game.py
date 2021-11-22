# holds game logic
import numpy as np
from threading import Thread
from queue import Queue

from Board import Board
from HumanPlayer import HumanPlayer
from GUIHumanPlayer import GUIHumanPlayer
from RandomPlayer import RandomPlayer
from Field import GUI

CONNECTED_VECTORS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, -1), (-1, 1)]


class Game(Thread):
    """
    Class Game holds most of the game logic such as the win condition and is able to check whether a move is legal.
    """
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.blue_player = RandomPlayer(2)
        self.red_player = GUIHumanPlayer(1)
        self.blue_player_turn = True
        self.next_move = None
        self.swap_rule = True
        self.first_move = True
        self.gui = None
        if isinstance(self.blue_player, GUIHumanPlayer) or isinstance(self.red_player, GUIHumanPlayer):
            self.queue = Queue()
            self.gui = GUI(self.board, self.queue_move)
            if isinstance(self.blue_player, GUIHumanPlayer):
                self.blue_player.pass_access_to_queue(self.get_move_from_queue)
            if isinstance(self.red_player, GUIHumanPlayer):
                self.red_player.pass_access_to_queue(self.get_move_from_queue)
            self.start()
            self.gui.main_loop()
        else:
            self.run()

    def run(self):
        self.play_game()

    def game_finished(self, player_color: int) -> bool:
        """
        Function to check if a certain player won the game
        :param player_color: red = 1, blue = 2, empty = 0
        :return:
        """
        # flood fill algorithm
        # Fip board if looking at the other player
        board_mat = self.board.board_state if player_color == 2 else self.board.board_state.T
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

    def check_move(self, x: int, y: int, color: int) -> bool:
        if self.swap_rule:
            self.swap_rule = False
            return True
        else:
            if self.board.board_state[x, y] == 0:
                return True
            else:
                return False

    def make_move(self, x, y, color: int):
        if self.first_move:
            self.board.make_move(x, y, color)
            self.first_move = False
        elif self.check_move(x, y, color):
            self.board.make_move(x, y, color)
        else:
            print("Invalid move, choose again.")

    def queue_move(self, x, y):
        self.queue.put((x, y))

    def get_move_from_queue(self):
        return self.queue.get()

    def play_game(self):
        red_won = self.game_finished(1)
        blue_won = self.game_finished(2)
        while not red_won and not blue_won:
            if self.blue_player_turn:
                x, y = self.blue_player.get_move(self.board)
                self.board.make_move(x, y, 2)
            else:
                x, y = self.red_player.get_move(self.board)
                self.board.make_move(x, y, 1)
            self.blue_player_turn = not self.blue_player_turn
            red_won = self.game_finished(1)
            blue_won = self.game_finished(2)
        if red_won:
            print("Red (1) won")
        else:
            print("Blue (2) won")

    def get_board_state(self):
        return self.board.board_state


if __name__ == '__main__':
    game = Game()
