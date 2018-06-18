from exturtle import *          # Import all the exturtle functions 
t = Turtle()
hideturtle(t)
t.speed(0)
S = 'A'
n = 10
step = 2
rules = {'A':'AB', 'B' : 'A'}   #rules for algae
def srs_print(S,n,rules):
    """Re-write an axiom according to given rules where S is the axiom
     or first string to be re-written, n is the number of re-writes and rules
     is a dictionary with the key as the initial character and the value is the
     character(s) to be re-written to"""
    
    for i in range (n):                     #for the total amount of re-writes
        newaxiom = ''
        for i in S:                         #for each character in the string                        
            for k, v in rules.items():      
                if i ==k:                   #when a character matches a key in the dictionary
                    newaxiom += v           #add the dictionary value to newaxiom
        if i not in rules.keys():
            newaxiom+= i                    #otherwise add keep the character as it is
        S = newaxiom                        # replace the original string with the re-written one
    
       
    return S    



def srs_draw(S, n, t, rules, step, angle):
    """Turn string into turtle movement where S is the string to be drawn,
     n is the number of times the string is to be re-written, t is a turtle, rules
     is a dictionary with the key as the initial character and the value is the
     character(s) to be re-written to, step is the distance the turtle with move
     in a straight line, and angle is the amount of degrees the turtle will rotate"""
    
    for letter in S:                        
        if letter == 'E' :
            forward(t, step)
        if letter == 'F':
            forward(t,step)                 #carry out these movemnet rules
        if letter == 'L':                   #for each character in the string S
            left(t, angle)
        if letter == 'R':
            right(t, angle)
    
print(srs_print(S,n,rules))                 #print the string re-written for algae


rules = {'E':'FLELF', 'F':'ERFRE','L':'L','R': 'R'}     #Sierpinski rules
n = 5
S = 'E'
S= srs_print(S,n,rules)
print(srs_draw(S, n, t, rules, step,angle= 60))           #draw Sierspinski
