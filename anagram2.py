
def make_anagram_dict(words):
    anagramdict = {}
    for i in words:
        
        key = get_key(i)
        if key not in anagramdict:
            anagramdict[key] = [i]
        else:
            current = anagramdict[key]
            current.append(i)
            anagramdict[key] = current
    longest = sorted(anagramdict.values(), key=len)[-1][0]
    print('the longest is',longest)
    count = 0
    for i, k in anagramdict.items():
        if len(i) > count:
            count = len(i)
            biggest = k


    return anagramdict, biggest 



def anagram_dict_from_file(file):
    wordslist = []
    lines = open(file,'r').readlines()
    for i in lines:
        i = i.strip().lower()
        wordslist.append(i)
        
    return wordslist
                
def get_key(i):
    
    key = list(i)
    key = sorted(key)
    key = "".join(key)
    return key
    

if __name__ == '__main__':
    word = anagram_dict_from_file('words.txt')
    print(make_anagram_dict(word))
 