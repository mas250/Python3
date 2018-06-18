def eapprox(number):
    factorial = 1
    total = 1
    for i in range (1, number+1):
        
        factorial = factorial * i
        total = 1 / factorial + total
    return factorial

    print(total)
from math import e

number = int(input("enter  number" ))

eapprox(number)
etol = 0.001

while e - factorial > etol:
    print (e)

    
print (e)


