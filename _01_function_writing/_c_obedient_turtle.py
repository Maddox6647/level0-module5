"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, megagon, and
    #      circle.
    #   3. Ask the user for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    shrekyduckiee = turtle.Turtle()
    mega_shapes = simpledialog.askstring(title='shrek', prompt='what shape would you like to draw, triangle, square, megagon, circle')
    if mega_shapes == 'megagon':
        for i in range(1000000):
            shrekyduckiee.speed(0)
            shrekyduckiee.circle(1000)
            shrekyduckiee.forward(10)
    elif mega_shapes == 'square':
        for i in range(4):
            shrekyduckiee.speed(1)
            shrekyduckiee.right(90)
            shrekyduckiee.forward(500)
    elif mega_shapes == 'circle':
        shrekyduckiee.speed(1)
        shrekyduckiee.circle(1000)









