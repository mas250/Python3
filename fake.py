count = 0
longest = ''
filename = 'drus.py'
try:
    f = open(filename, 'r')
    lines = f.readlines()
    for line in f:
        words = line.split('\n')
        print (words[5])
        print(words)
    f.close()
except:
    print('not there')
