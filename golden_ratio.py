from math import sqrt
prev = 1
L    = [prev]
diff_list = []
for n in range (19):
    rooted_number = sqrt(prev + 1)
    L.append(rooted_number)
    prev = rooted_number

for i in L:
    diff = (1 + sqrt(5))/2 - i
    diff_list.append(diff)

for i in diff_list:
    print(i)
