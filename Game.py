# holds game logic
import networkx as nx

from Board import Board
from HumanPlayer import HumanPlayer
from RandomPlayer import RandomPlayer


class Game:
    def __init__(self):
        self.board = Board(4)
        self.blue_player = RandomPlayer("blue")
        self.red_player = HumanPlayer("red")
        self.blue_player_turn = True

    def game_finished(self, player_color) -> bool:
        isolated = self.board.G.subgraph([n for n in self.board.G.nodes if self.board.colors[n] == player_color])
        if player_color == "red":
            if any([nx.has_path(isolated, x, y) for (x, y) in self.board.red_side if (x in isolated and y in isolated.nodes)]):
                print(player_color, "wins!")
                return True
        else:
            if any([nx.has_path(isolated, x, y) for (x, y) in self.board.blue_side if (x in isolated and y in isolated.nodes)]):
                print(player_color, "wins!")
                return True
        return False

    def check_move(self, index, player) -> bool:
        # is this move legal
        return True

    def play_game(self):
        while not self.game_finished("red") or not self.game_finished("blue"):
            if self.blue_player_turn:
                self.board.make_move(self.blue_player.get_move(self.board), "blue")
            else:
                self.board.make_move(self.red_player.get_move(self.board), "red")
            self.blue_player_turn = not self.blue_player_turn


if __name__ == '__main__':
    game = Game()
    game.play_game()
# game.board.draw_boad()
    # game.board.make_move(1, "red")
    # game.board.make_move(0, "red")
    # game.board.make_move(5, "red")
    # game.board.make_move(9, "red")
    # game.board.make_move(13, "red")
    # game.board.make_move(14, "red")
    # game.board.draw_boad()
    #
    # print(game.game_finished("red"))
