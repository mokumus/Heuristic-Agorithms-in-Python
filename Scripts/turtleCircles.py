import turtle
import greedy
import utilities

class MyTurtle(turtle.Turtle):
    def __init__(self, width=1000, height=500, startx=None, starty=None):
        turtle.Turtle.__init__(self)
        turtle.bgcolor("black")
        self.color("white")

        turtle.title("Circle Packing Visualization")
        turtle.setup(width, height, startx, starty)

    def drawCircle(self, x, y, radius=50):
        self.penup()
        self.setposition(x, y)
        self.pendown()
        self.circle(radius)

    """
    Draws circles with the provided positions

    arguments:
        positions -- list of mutable pairs, [offset, radius]
    """
    def drawCircles(self, positions, offsetx = -400, offsety = -130):
        for position in positions:
            self.drawCircle(position[0] + offsetx, offsety, position[1])

if __name__ == "__main__":


    test1 = [[0, 90], [0,10]]
    result = greedy.greedy(test1)
    result = utilities.writeOffsets(result)
    t = MyTurtle()
    t.color("White")
    t.drawCircles(result)
    t.getscreen()._root.mainloop()





