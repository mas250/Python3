
def make_anagram_dict(words):
    '''Create a dictionary from the list words. The dictionary will have
    the string from words in alphabetical order as the key, with the original
    word and any anagrams as the values'''
    
    anagramdict = {}
    for i in words:
        key = get_key(i)                        #format the key, more detail in function
        if key not in anagramdict:
            anagramdict[key] = [i]              
        else:
            current = anagramdict[key]
            current.append(i)
            anagramdict[key] = current
    longest = sorted(anagramdict.values(), key=len)[-1][0]      #sorts the list in ascending order
    print('the longest is',longest)                             # of key value, the last will be largest
    
    for i in anagramdict.keys():
        findgram(i, anagramdict)                                #keep finding anagrams

    
 
    
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

def anagram_dict_from_file(file):
    '''create a dictionary from a text file which is the variable file. The dictionary will have
    the string from words in alphabetical order as the key, with the original
    word and any anagrams as the values'''
    
    wordslist = []
    lines = open(file,'r').readlines()
    for i in lines:
        i = i.strip().lower()                   #re-write to lowercase
        wordslist.append(i)
        
    return wordslist
                
def get_key(i):
    '''turns the string from the list into an alphabetical string where i is
    an element from the list of words'''
    
    key = list(i)                               #seperate each charater
    key = sorted(key)                           #use sorted to place in order                          
    key = "".join(key)                          #re-combine orderd list of charaters to a string

    return key
    
if __name__ == '__main__':
##    word = ['carthorse','madden']             # these lines are uncommented for as a debuging test for a programmer
##    print(make_anagram_dict(word))            
    word = anagram_dict_from_file('words.txt')
    make_anagram_dict(word)
 
