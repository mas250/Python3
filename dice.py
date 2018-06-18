from random import random

def roll(user_die):
    """return a random number from 1 to 6"""

    x = random()
    x = int(x*user_die) + 1

    return x

def test_roll(N=6000):
    """Test roll() N times"""
    dieList = []
    for i in range (user_die):
        dieList.append(i+1)
    
    count = [0] * (user_die + 1)    

    for i in range(N):
        j = roll(user_die)
        assert j in dieList
        count [j] = count[j] + 1

    for i in range(user_die + 1):
        print(i, count[i])

def choose(L):
    """return item at random from list"""

    if len(L) == 0:
        
        return None
    x = random()
    i = int(x*len(L))
    assert 0 <= i < len(L)
    return L[i]
            

def throw(dice = 1):
    """throw dice, returning the sum"""

    sum = 0
    for n in range (dice):
        sum = sum + roll()
    return sum
#user_die = 6
##user_die = int(input('Enter number of faces on dice: '))
#test_roll()
