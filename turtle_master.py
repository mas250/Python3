#    Matthew Shaw
#    Sunday, 1 November 2015 at 16:35:35
#    Ring.py


from exturtle import *          # Import all the exturtle functions 

from math import cos, sin, pi
turtle = Turtle()



def star(turtle,x, y, points, R, r):
    """
    Use exturtle to draw a star centred around coordinates (x, y)
    with points as the number of points, R as the distance from the centre
    to the far point and r to the closer edge
    """
    
    penup(turtle)                                            

    theta = (2 * pi) / points               # Angle              
    
    for i in range (0, points+1) :          # Draw the coordinates
                                            # for each point
                            
        
        point_n = (i * (2*pi))/points
        
        
        goto(turtle, r * sin((i - 1/2)*theta) + x, r * cos((i-1/2)*theta)+y)   # Equation given in appendix, more effecient than goto function  
        pendown(turtle)
        goto(turtle, R * sin(point_n)+x, R * cos(point_n)+y)


def ring(turtle, cx,cy,Nstars,radius,points, R, r):
    """
    Draw a circle centered at points (cx, cy), putting Nstars number of points
    around the circle with a radius, radius. the stars will have
    points number of points, R as the distance from the centre
    to the far point and r to the closer edge
    """

    theta = (2 * pi) / Nstars
    
    for i in range (Nstars):                # Keep drawing stars at the points
        x = radius * sin (i * theta) +cx    # around the circle
        y = radius * cos (i * theta) +cy
        star(turtle, x, y, points, R, r)        
        
    

#star(turtle,-100,-100,5,100, 50)
ring(turtle, 0, 0, 12, 200, 5, 50, 25)
#mainloop()
