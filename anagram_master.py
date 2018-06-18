
def make_anagram_dict(words):
    '''create a dicitionary from the list words. The dictionary will have
    the string from words in alpahabetical order as the key, with the original
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
    longest = sorted(anagramdict.values(), key=len)[-1][0]      #sorts the list in asending order
    print('the longest is',longest)                             # of key value, the last will be largest
     
    return anagramdict 


def anagram_dict_from_file(file):
    '''create a dicitionary from a text file which is the variable file. The dictionary will have
    the string from words in alpahabetical order as the key, with the original
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
    word = anagram_dict_from_file('words.txt')
    make_anagram_dict(word)
 
