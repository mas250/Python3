from anagram import *



def make_anagram_dict(word):
    '''create a dictionary from the list words. The dictionary will have
    the string from words in alphabetical order as the key, with the original
    word and any anagrams as the values'''
    
    anagramdict = {}
    
    key = get_key(word)                        #format the key, more detail in function
    if key not in anagramdict:
        anagramdict[key] = [word]              
    else:
        current = anagramdict[key]
        current.append(word)
        anagramdict[key] = current

    for i in anagramdict.keys():
        findgram(i, anagramdict)
        print(list(anagramdict.values()))                            # of key value, the last will be largest
    
    return anagramdict

def findgram(i, anagramdict):
    '''this function takes all the keys from the dictionary anagramdict created in make_anagram_dict as i
    and will continually find anagrams for the key'''
    
    anagramlist=[]
    filename = 'words.txt'
    f = open(filename, 'r')
    line = f.readline()
    for k in f:                                                 #cycle through the word file, if the word in the text file                                                
            matchgram = sorted(k.strip('\n'))                   #matches the key alphabetically,
            if sorted(i) == matchgram:                          #add the unordered word from the file, to the dictionary as a value
                anagramlist.append(k.strip('\n'))
                anagramdict.update({i:anagramlist})             #this will take a long time to complete with the entire word file as a dictionary(!)            


def get_key(i):
    '''turns the string from the list into an alphabetical string where i is
    an element from the list of words'''
    
    key = list(i)                               #separate each character
    key = sorted(key)                           #use sorted to place in order                          
    key = "".join(key)                          #re-combine ordered list of characters to a string

    return key
def anaquery():
    file = 'words.txt'
    lines = open(file,'r').readlines()
    while True:
        anagram_to_find = input("Enter a word to find it's anagrams (if any): ")
        make_anagram_dict(anagram_to_find)
        
        
print(anaquery())
