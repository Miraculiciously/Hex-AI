from threading import Thread
import tkinter as tk
from math import cos, sin, radians, sqrt

COLORS = {0: "white", 1: "red", 2: "blue"}


class GUI:
    def __init__(self, board, queue_move):
        # Initialise all that the board needs
        self.board = board
        self.queue_move = queue_move
        self.N = board.N

        self.app = tk.Tk()
        self.side_length = 30
        # TODO this needs to be adapted according to the scale but I'm working on it maybe tonight
        self.frame_boundary = 1 / sqrt(2) * self.side_length
        # add canvas width and height
        self.height = self.frame_boundary / 2 + (self.N - 1) * self.side_length * (1 + 1 / sqrt(2))
        self.width = self.frame_boundary + (self.N + self.N / 2) * self.side_length * sqrt(3)
        self.canvas = tk.Canvas(self.app, width=self.width, height=self.height)

    def hex_coordinates(self, x, y):
        points = [x, y]
        for n in range(5):
            points.append(points[2 * n] + self.side_length * sin(radians(60 * n)))
            points.append(points[2 * n + 1] + self.side_length * cos(radians(60 * n)))
        return points

    def draw_field(self) -> None:
        # draw canvas boundaries
        self.canvas.create_polygon(0, 0, sqrt(3) * (self.N + 0.3) * self.side_length, 0, self.width / 2,
                                   self.height / 2, fill="red")
        self.canvas.create_polygon(self.width, self.height, self.width / 2, self.height / 2,
                                   self.width - sqrt(3) * (self.N + 0.3) * self.side_length, self.height, fill="red")
        self.canvas.create_polygon(0, 0, 0, self.height, self.width - sqrt(3) * (self.N + 0.3) * self.side_length,
                                   self.height, self.width / 2, self.height / 2, fill="blue")
        self.canvas.create_polygon(self.width, 0, sqrt(3) * (self.N + 0.3) * self.side_length, 0, self.width / 2,
                                   self.height / 2, self.width, self.height, fill="blue")
        self.canvas.pack()
        for x in range(self.N):
            for y in range(self.N):
                polygon = self.canvas.create_polygon(
                    *self.hex_coordinates(
                        self.frame_boundary + sqrt(3) * self.side_length * (x + y / 2),
                        self.frame_boundary + 1.5 * y * self.side_length
                    ),
                    fill=COLORS[self.board.board_state[x, y]],
                    outline="black",
                    width=1.25
                )
                self.canvas.tag_bind(polygon, "<Button-1>", lambda e, x=x, y=y: self.on_polygon_click(x, y))
        self.app.update()

    def on_polygon_click(self, x, y):
        # print("polygon click", x, y)
        self.queue_move(x, y)

    def main_loop(self):
        # TODO move over to calling mainloop in the main thread instead of update in a while True
        while True:
            self.draw_field()


# if __name__ == '__main__':
#     gui = GUI()
#     # gui.make_move(0, 0, 1)
#     # gui.make_move(3, 3, 1)
#     # gui.make_move(4, 4, 2)
#     while True:
#         gui.draw_field()
