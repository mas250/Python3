a = [0.04904772, 1.38633599, 0.94084723, -0.96782833, -0.66058869]
b = [1.07227778, -0.75143678, 0.54550933, 0.20866252, -1.4619395]

def dot (a,b):
    S = 0
    if len(a) == len(b):
        
        for i in range (len(a)):
            S = (a[i] * b[i]) + S
    print (S)
    
        
    if len(a) != len(b):
        print ("lists do not match")
       
    
dot(a,b)
