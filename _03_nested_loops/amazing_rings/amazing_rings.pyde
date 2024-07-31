"""
Go to the recipe to run the demonstration before starting this program
"""
speed = 20
x=200
def setup():
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(800, 400)
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
    frameRate(20)
def draw():
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window.
    global x
    global speed
    background(255, 220, 18)
    for i in range(400, 0, -300):
        ellipse(x,200,i,i)
    x += speed

    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    #       Then increase x by the amount in speed.
    
    
    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */
    if x >= 800:
        speed = -speed 
    if x <= 0:
        speed = -speed 
    # When the rings reach the left side of the sketch, reverse the direction again
        
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
        
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
