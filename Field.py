import tkinter as tk
from math import cos, sin, radians

from networkx.drawing.nx_pylab import draw

from Board import Board

class GUI:
    def __init__(self):
        self.app=tk.Tk()
        self.canvas=tk.Canvas(self.app) 
        self.scale =  20
        self.frame_boundary = 20 # this needs to be adapted according to the scale but I'm working on it maybe tonight
        # add canvas width and height
        
        # Add line for player colours
        #self.canvas.create_line(10, 10, x_end, 10, fill="blue")

    # def draw_hexagon(self, x, y) -> None:
    #     x_start = x
    #     y_start = y
    #     for n in range(6):
    #         x_end = x_start + self.scale * sin(radians(60*n))
    #         y_end = y_start + self.scale * cos(radians(60*n))
    #         self.canvas.create_line(x_start, y_start, x_end, y_end, fill="black")
    #         x_start = x_end
    #         y_start = y_end

    def hex_coordinates(self, x, y):
        points = [x, y]
        for n in range(5):
            points.append(points[2*n] + self.scale * sin(radians(60*n)) )
            points.append(points[2*n + 1] + self.scale * cos(radians(60*n)) )
        return points

    def draw_field(self) -> None:
        self.canvas.pack()
        for x in range(board.N):
            for y in range(board.N):
                self.canvas.create_polygon(
                    *self.hex_coordinates(
                        self.frame_boundary + 2.25*self.scale*(x+y/2) * sin(radians(60)),
                        self.frame_boundary + y*1.6875*self.scale
                        ),
                        fill= "white",
                        outline = "black"
                    )
        
        self.app.mainloop()    


if __name__ == '__main__':
    board = Board()
    gui = GUI()
    gui.draw_field()