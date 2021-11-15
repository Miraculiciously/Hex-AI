import tkinter as tk
from math import cos, sin, radians, sqrt



class GUI:
    def __init__(self, N=11):
        # Initialise all that the baord needs
        self.N = N
        self.colors = ['white' for n in range(N**2)]

    def hex_coordinates(self, x, y):
        points = [x, y]
        for n in range(5):
            points.append(points[2*n] + self.side_length * sin(radians(60*n)) )
            points.append(points[2*n + 1] + self.side_length * cos(radians(60*n)) )
        return points

    def draw_field(self) -> None:
        # Initialise canvas
        self.app=tk.Tk()
        self.side_length =  30
        self.frame_boundary = 1/sqrt(2)*self.side_length # this needs to be adapted according to the scale but I'm working on it maybe tonight
        # add canvas width and height
        self.height = self.frame_boundary/2 + (self.N-1)*self.side_length*(1+ 1/sqrt(2))
        self.width = self.frame_boundary + (self.N + self.N/2) * self.side_length*sqrt(3)
        self.canvas=tk.Canvas(self.app, width = self.width, height = self.height)
        # draw canvas boundaries
        self.canvas.create_polygon(0,0, sqrt(3)*(self.N+0.3)*self.side_length, 0, self.width/2, self.height/2, fill = "red")
        self.canvas.create_polygon(self.width,self.height, self.width/2, self.height/2, self.width - sqrt(3)*(self.N+0.3)*self.side_length, self.height, fill = "red")
        self.canvas.create_polygon(0, 0, 0, self.height, self.width - sqrt(3)*(self.N+0.3)*self.side_length, self.height, self.width/2, self.height/2, fill = "blue")
        self.canvas.create_polygon(self.width, 0, sqrt(3)*(self.N+0.3)*self.side_length, 0, self.width/2, self.height/2,self.width, self.height,  fill = "blue")
        self.canvas.pack()
        for x in range(self.N):
            for y in range(self.N):
                self.canvas.create_polygon(
                    *self.hex_coordinates(
                        self.frame_boundary + sqrt(3)*self.side_length*(x+y/2),
                        self.frame_boundary + 1.5*y*self.side_length
                        ),
                        fill= self.colors[y*self.N + x],
                        outline = "black",
                        width = 1.25
                    )
        
        self.app.mainloop()
    
    def make_move(self, index, color: str):
        assert(color == "red" or color == "blue")
        self.colors[index] = color


if __name__ == '__main__':
    gui = GUI()
    gui.draw_field()
    #gui.make_move(3, "red")
    #gui.draw_field()
