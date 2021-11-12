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
                if  not 0 <= selected <= board.N**2 - 1:
                    print("It has to be an integer between 0 and", board.N**2 -1)
                    selected = None
            except ValueError:
                print("It has to be an integer between 0 and", board.N**2 -1)
        return selected

if __name__ == "__main__":
    board = Board(4)
    humanplayer = HumanPlayer("red")
    humanplayer.get_move(board)