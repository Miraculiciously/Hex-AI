from Board import Board


class HumanPlayer:
    def __init__(self, color: str):
        self.own_color = color

    def get_move(self, board: Board):
        board.draw_boad()
        selected = None
        print("Your color is " + self.own_color)
        while selected is None:
            try:
                selected = int(input("Select field: "))
                # Is the selection valid in itself and within the range?
            except ValueError:
                print("It has to be a number")
        return selected