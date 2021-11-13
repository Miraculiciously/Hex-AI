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
                split_move = input("Select x and y of field (x, y): ").split(",")
                selected = (int(split_move[0]), int(split_move[1]))
                # Is the selection valid in itself and within the range?
            except ValueError:
                print("It has to be 2 numbers separated by a ','")
            except IndexError:
                print("Please type 2 numbers separated by a ','")
        return selected