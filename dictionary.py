D = [ (678, 678, 'value'), (290179560907415603, 'a key', 100),  (8547278478136085765, 'another key', 101)  ]

def insert(key, value, D, hasher = hash):
    '''insert the (key,value) pair into the dictionary D and with a hash value hasher'''
    tup = (key, value)                      #place key and value into a tuple
    hasher = hash(key)
    tup = (hasher,) + tup                   #combine a hash into the tuple
    D.append(tup)
    return D


def get(key, D, hasher = hash):
    
    '''retrieve the (key,value) pair into the dictionary D and with a hash value hasher'''
    for item in D:                          #cycle through the dictionary
        if key in item:                     #return the key for where i is a tuple and [2] is the
            return item[2]                  #index inside the tuple of the hash
    if key not in item:
        raise KeyError('Key not found')

     
def pop(key, D, hasher = hash):
    '''return and remove the (key,value) pair into the dictionary D and with a hash value hasher'''
    for item in D: 
        count = 0                           #increment count until the specified key is found
        count+=1                            #this is so count can be used as the index
        if key in item:
            D.pop(count)
            return item[2]
            
            break


def keys(D):
    '''return a list of the keys in D'''
    
    keylist = []
    for i in range(len(D)):                 #cycle through the dictionary
        keylist.append(D[i][1])             #return the key for where i is a tuple and [1] is the
    return keylist                          #index inside the tuple of the key


def values(D):
    '''return a list of the values in D'''
    
    valuelist = []
    for i in range(len(D)):                 #cycle through the dictionary
        valuelist.append(D[i][2])           #return the value for where i is a tuple and [2] is the
    return valuelist                        #index inside the tuple of the key


def items(D):
    '''return a list of the items in D'''
    
    itemlist = []
    for i in range(len(D)):
        itemlist.append(D[i])
    return itemlist


