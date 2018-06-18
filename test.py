S = 'A'
n = 10
rules = {'A':'AB', 'B' : 'A'}
def srs_print(S):
    """Re-write an axiom according to given rules"""
    newaxiom = ''
    for i in S:
##        if i in rules.items():
##            newaxiom +=
        for k, v in rules.items():
            if i ==k:
                newaxiom += v                               
##        if i is 'B':
##            newaxiom +='A'          #append newaxiom according to the rules of rewriting the string
    S = newaxiom
##    print(axiom)          Uncomment to see the axiom re-written each time
    return S            #(above line can crash computer with 30 re-writes)

def give_back(S, n):
    '''Keep re-writing an axiom a number of times by calling the function algae'''
    for i in range (n):
        S = srs_print(S)
    return S
        
print( S)
print(give_back(S, n))
print(len(give_back(S, 30)))

