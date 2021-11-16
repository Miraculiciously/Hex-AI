from Board import Board


class HumanPlayer:
    def __init__(self, color: int):
        self.own_color = color

    def get_move(self, board: Board):
        board.draw_boad()
        selected = None
        print("Your color is " + self.own_color)
        while selected is None:
            try:
                split_move = input("Select x and y of field (x, y): ").split(",")
                selected = (int(split_move[0]), int(split_move[1]))
                if not (0 <= selected[0] < board.N and 0 <= selected[1] < board.N):
                    raise ValueError()
                # Is the selection valid in itself and within the range?
            except (ValueError, IndexError):
                print("It has to be 2 integers between 0 and ", board.N - 1, " separated by a ','")
        return selected


if __name__ == "__main__":
    board = Board(4)
    humanPlayer = HumanPlayer(1)
    humanPlayer.get_move(board)
