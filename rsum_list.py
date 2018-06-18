def rsum(n):
    limit=len(n)-1
    newsum = n[0] + n[limit]
    for i in range (limit-1,0,-1):
        newsum = newsum + n[i]
        
    return newsum

n = [1,2,3,4,5,6]

print(rsum(n))
