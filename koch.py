from exturtle import *

t = Turtle()
t.speed(0)

def draw(t,n,L):
    if n ==0:
        forward(t,L)
##    for i in range (n):
##        right(t,90)
##        forward(t, L/3)
##        right(t,120)
##        forward(t,L/3)
##        left(t,60)
##        forward(t,L/3)
##        draw(t,n-1, L)



    else:
        n=n-1
        draw(t,n, L/3)
        
        left(t,60)
        draw(t,n, L/3)
        right(t,120)
        draw(t,n, L/3)
        left(t,60)
        draw(t,n, L/3)
draw(t,5,500)
