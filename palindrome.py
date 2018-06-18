lines = open('lowercasewords.txt', 'r').readlines()
def palindrome(s):
    return s == s[::-1]


for line in lines:
    words = line.strip()

    if len(words) >=3 and palindrome(words):
        print(words)
