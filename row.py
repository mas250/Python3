from exturtle import *          # Import all the exturtle functions 

from math import cos, sin, pi, sqrt
turtle = Turtle()



def star(turtle,x, y, points, R, r):
 #   r = R * ((3 - sqrt(5) / 2))
    
    penup(turtle)

    theta = (2 * pi) / points
    
    for i in range (0, points+1) :
        
        
        
        point_n = (i * (2*pi))/points
        
        
        goto(turtle, r * sin((i - 1/2)*theta) + x, r * cos((i-1/2)*theta)+y)
        pendown(turtle)
        goto(turtle, R * sin(point_n)+x, R * cos(point_n)+y)
 
    

star(turtle,-250,0, 5, 50, 25)
star(turtle,-100,0, 6, 50, 25)
star(turtle,50,0,7,50, 25)
star(turtle,200,0,8,50, 25)


