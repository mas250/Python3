def bracket_check(brackets):
    '''function for checking a string of brackets'''
    o = [ '{', '[', '(' ]
    c = [ '}', ']', ')' ] 
    l = []
    check = 0
    
    for i in brackets:
        if i in o:
            check += 1
        if i in c:
            check -= 1
    if check == 0:
        print('yep')
    else:
        print('nah')
    
            


bracket_check('8x8y[E(x,y) ! [(P(x) ! P(y)) ! (P(y) ! P(a)]]')
