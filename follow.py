from exturtle import *          # Import all the exturtle functions 
t = Turtle()
hideturtle(t)
t.speed(0)

def follow(t, S, stack, step=10, angle=90):
    """Turn string into turtle movement"""
    for letter in S:                
        if letter == 'E' :
            forward(t, step)
        if letter == 'F':
            forward(t,step)             
        if letter == 'L':
            left(t, angle)
        if letter == 'R':
            right(t, angle)

if __name__ == '__main__':          
    S = 'ELFLLFRERREERFLLRELFFLLFLERRERFLLRELFFLLFLERRERFRELFLLFRERREERFLRRELFLLFRERREERFLELFLLFRERREERFLRRELFFLLFLERRERFL'
    follow(t, S,stack = [], step = 4, angle = 60)
#if this program is run without being imported
#perform a short test
