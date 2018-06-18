from math import sqrt
prev = 1
L = [prev]

for n in range (19):
    rooted_number = sqrt(prev + 1)
    L.append(rooted_number)
    prev = rooted_number

for i in L:
    print(i)
