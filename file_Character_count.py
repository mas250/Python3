
#    Matthew Shaw
#    Friday, 9 October 2015 08:45:50

#    A program to count the words and characters in a list

rhyme_length = 0
lines = open('dictionary.txt', 'r').readlines()
word_count = len(lines)                     # asign the number of words
for i in lines:                             # iterate through text file
    
    list(i)
    
    rhyme_length = rhyme_length + len(i)


#print ('The number of words in this file are: ' , word_count)
print ('''The number of characters excluding new new line characters is: ''' ,  rhyme_length - word_count)

avarage_word_length =   (rhyme_length - word_count) / word_count
print ('the avarage length of each word is: ' , avarage_word_length)
