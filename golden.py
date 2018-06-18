from math import sqrt
gList = [1]
def golden(N):
    
    
    lastI = 0
    for i in range(0,N):
        

        gList.append(sqrt(gList[i]+1))
    print(gList)
    return gList

golden(10)
gRatio = (1+ (sqrt(5)))/2
error = []
for n in range (len(gList)):
    diff = abs(gList(n) - gRatio )
    error.append(diff)
ptint(error)
