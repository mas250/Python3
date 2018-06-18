def pig(word):
    """Translte a word into pig latin"""
    piglist = list(word)
    vowelcheck = False
    
    for i in piglist:
        
        if piglist[0] != 'a' and piglist[0] != 'e' and piglist[0] != 'u' :
        
            piglist.append(piglist.pop(0))
                
    
    piglatin=''.join(map(str, piglist))
    print (piglatin+'ay')
    
pig('pluck')
