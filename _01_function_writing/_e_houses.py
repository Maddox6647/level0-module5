"""
Have the turtle draw a row of houses.
"""
from tkinter import messagebox, simpledialog, Tk

import turtle
def draw_pointy_roof():
    turtle_man.right(-45)
    turtle_man.forward(25)
    turtle_man.right(90)
    turtle_man.forward(25)
    turtle_man.right(45)
def draw_house(size):
    turtle_man.pencolor('brown')
    if size == 'small':
        turtle_man.forward(25)
        turtle_man.right(90)
        draw_pointy_roof()
        turtle_man.forward(25)
        turtle_man.right(-90)
        turtle_man.pencolor('green')
        turtle_man.forward(19)
        turtle_man.right(-90)

    elif size == 'mega':
        turtle_man.pencolor('brown')
        turtle_man.forward(400)
        turtle_man.right(90)
        draw_pointy_roof()
        turtle_man.forward(400)
        turtle_man.right(-90)
        turtle_man.pencolor('green')
        turtle_man.forward(19)
        turtle_man.right(-90)

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    turtle_man = turtle.Turtle()
    turtle_man.penup()
    turtle_man.goto(x=-400, y=-360)
    turtle_man.left(90)
    turtle_man.pendown()
    size = simpledialog.askstring(title='r', prompt='small or mega')
    for i in range(23):
        size = simpledialog.askstring(title='r', prompt='small or mega')
        draw_house(size)

    window.mainloop()

    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.

