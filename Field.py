import tkinter as tk
from math import cos, sin, radians

from networkx.drawing.nx_pylab import draw

from Board import Board

class GUI:
    def __init__(self):
        self.app=tk.Tk()
        self.canvas=tk.Canvas(self.app)

    def draw_hexagon(self, x, y):
        length = 10
        x_start = x
        y_start = y
        for n in range(6):
            x_end = x_start + length * cos(radians(60*n))
            print(x_end)
            y_end = y_start + length * sin(radians(60*n))
            self.canvas.create_line(x_start, y_start, x_end, y_end, fill="black")
            x_start = x_end
            y_start = y_end

    def draw_field(self) -> None:
        self.canvas.pack()
        self.draw_hexagon(50,50)
        self.app.mainloop()    

# class cell:
#     def __init__(self, x, y, color: str):
#         self.x = x
#         self.y = y
#         self.color = color
    
#     def draw(self):
#         x_start = self.x
#         y_start = self.y
#         for n in range(6):
#             x_end = x_start + cos(radians(60*n))
#             y_end = y_start + cos(radians(60*n))
#             self.parent.create_line(start_x, start_y, end_x, end_y, fill=self.color)
#             x_start = x_end
#             y_start = y_end

if __name__ == '__main__':
    gui = GUI()
    gui.draw_field()