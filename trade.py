lines = open('trader.txt', 'r').readlines()
pos_count = 0
neg_count = 0
bonus     = 0
day = 0
for line in lines:
    words = line.strip()
    num = float(words)
    

    if num > 0:
        pos_count = pos_count + 1
        bonus = num + bonus
        if bonus >= 200000:
            print ("bonus paid on day" , day)
            bonus = 0
   

    if num < 0:
        neg_count = neg_count + 1
        bonus = num - bonus
    day = day + 1

print( pos_count/neg_count)
print( "the bonus is", bonus)
print()
print (day)
