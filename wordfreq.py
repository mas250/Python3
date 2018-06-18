# Print the frequencies with which words occur in a file. The results are
# printed with the words in the order that they occur in the file, but a
# dictionary is used to keep a count of the words. Counting does not start
# until a line starting with '***' has been seen and stops when another
# line with '***' is found, making the program suitable for Project
# Gutenberg files.

import string
def delete_punctuation(str):
    """
    Remove punctuation from a string, replacing it with a space
    """
    for p in string.punctuation:
        str = str.replace(p, ' ')
    return str

filename = 'dracula-full.txt'

f = open(filename, 'r')

words = []
count = {}

seenstars = False       # We haven't seen the first '***' line
while True:
    line = f.readline()
    if not line:
        print('EOF before second "***" line encountered')
        break
    if line[:3] == '***':
        if seenstars:
            break                       # Second '***' so finish
        else:
            seenstars = True
            continue                    # Don't process the first *** line

    if not seenstars:                   # Still in the preamble
        continue

    line = delete_punctuation(line).lower()
    for w in line.split():
        try:
            count[w] += 1
        except:
            count[w] = 1
            words.append(w)

for w in count:
    print('%20s%6d' % (w, count[w]))
    sorted(count.keys())
for w in range(50):
    print (count[w])
    
