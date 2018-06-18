from exturtle import *          # Import all the exturtle functions 
t = Turtle()
hideturtle(t)
t.speed(0)


def srs_print(S,n,rules):
    """Re-write an axiom according to given rules where S is the axiom
     or first string to be re-written, n is the number of re-writes and rules
     is a dictionary with the key as the initial character and the value is the
     character(s) to be re-written to"""
    
    for i in range (n):
        newaxiom = ''
        for i in S:                
            newaxiom += rules.get(i,i)      #if the charater in S is in the dictionary
        if i not in rules.keys():           #re-write according  to the dictionary value
            newaxiom += i                   #otherwise leave the character as it is
        S = newaxiom
    
       
    return S            



def follow(S, n, t, step, stack, angle):
    """Turn string into turtle movement where S is the string to be drawn,
     n is the number of times the string is to be re-written, t is a turtle, rules
     is a dictionary with the key as the inital character and the value is the
     character(s) to be re-written to, step is the distance the turtle with move
     in a straight line, and angle is the amount of degrees the turtle will rotate"""

    t.penup()
    t.setposition(0,-250)
    t.pendown()
    t.left(90)                              #better positioning for the fern
    for letter in S:
        
        if letter == 'F':
            forward(t,step)                 #for each character in the string S
        if letter == 'L':                   #carry out these movement rules                                                      
            left(t, angle)
        if letter == 'R':
            right(t, angle)
        if letter == '[':
            stack.append(t.position())
            stack.append(t.heading())       #add position and heading to the stack
            
        if letter == ']':
            heading = stack.pop()           
            position = stack.pop()          #get heading and stack while removing them from the stack
            t.penup()
            t.setposition(position)
            t.setheading(heading)           #move to the saved heading and position
            t.pendown()                     #without drawing, then get ready to draw
            


                
rules = {'A':'FL[[A]RA]RF[RFA]LA', 'F':'FF'}    #fern rules
n = 6
S = 'A'
step = 4
srs_print(S,n,rules)
S= srs_print(S,n,rules)
stack = []
print(follow(S, n, t, step, stack, angle = 25 ))
