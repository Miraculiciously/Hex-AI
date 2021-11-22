from Board import Board


class GUIHumanPlayer:
    def __init__(self, color: int):
        self.own_color = color
        self.get_move_from_queue = None

    def pass_access_to_queue(self, get_move_from_queue):
        self.get_move_from_queue = get_move_from_queue

    def get_move(self, board: Board):
        if self.get_move_from_queue:
            return self.get_move_from_queue()
        else:
            return 0, 0

