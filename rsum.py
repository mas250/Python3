def rsum(n):
    for i in range (n,1,-1):
        
        return n + rsum(n-1)
    return n
print(rsum(5))
