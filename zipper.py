a = [3, 4, 5, 6]
b = ['a', 'b', 'c', 'd']
def zipper(a,b):
    newZip = []
    if len (a) == len(b):
        for i in range(len(a)):
            newZip.append([a[i], b[i]])
    print (newZip)
    if len(a)!= len(b):
        print("lists do not match")
    
zipper(a,b)
