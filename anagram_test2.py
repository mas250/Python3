


def make_anagram_dict(words):
    import string

    filename = 'words.txt'

    f = open(filename, 'r')
    line = f.readline()

    anagramdict = {}
    anagramlist=[]
    sortlist=[]
    for i in words:
        
        j = (sorted(i))
        sortlist.append(j)
    ##    print(j)
        
        key = "".join(j)
        
        if key not in anagramdict:
            anagramlist = []
            anagramdict.update({key:j})
            
##        for item in sortlist:
         
    for k in f:
        l = sorted(k.strip('\n'))
        
        for i in range(len(sortlist)):
            j = sortlist[i]
            
            if l == j:
                
                
                anagramlist.append(k.strip('\n'))
                
                anagramdict.update({key:k})
                
                    
    
    return anagramdict
words = ['madden','carthorse']
print(make_anagram_dict(words))

