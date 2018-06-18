L = [1,2,2,3,]
L.sort()
L2=[]
def squeeze(L):
    

    last_i = None
    for i in L:
        
    
        if i != last_i:
            L2.append(i)
            last_i = i
    return L2

squeeze(L)
print (L2)
