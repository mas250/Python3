from exturtle import *          # Import all the exturtle functions 
t = Turtle()
hideturtle(t)
t.speed(0)
S = 'A'
n = 10
step = 2
rules = {'A':'AB', 'B' : 'A'}
def srs_print(S,n,rules):
    """Re-write an axiom according to given rules"""
    
    for i in range (n):
        newaxiom = ''
        for i in S:
            for k, v in rules.items():
                if i ==k:
                    newaxiom += v
        if i not in rules.keys():
            newaxiom+= i
             #append newaxiom according to the rules of rewriting the string
        S = newaxiom
    
       
    return S            #(above line can crash computer with 30 re-writes)



def follow(S, n, t, rules, step, angle):
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
    
print(srs_print(S,n,rules))


rules = {'E':'FLELF', 'F':'ERFRE','L':'L','R': 'R'}
n = 5
S = 'E'
S= srs_print(S,n,rules)
print(follow(S, n, t, rules, step,angle= 60))
