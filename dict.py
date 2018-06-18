import string
wordlist = [acehorrst
D = {}
L = []
for i in range(100):
    
    
##    file[i].split(' ')
    for s in string.punctuation:
       
       file[i] =file[i].replace(s, ' ')
##       file = file[i].split() 
    for i in file[i].split() :
   # 
        try:
                D[i] += 1
        except:
                D[i] = 1
                L.append(i)
for i in D:
    print('%20s%6d' % (i, D[i]))
