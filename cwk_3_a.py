prize_file_1 = open("/Users/MatBook/Downloads/prize1.txt")
List = []
prizes = []
for line in prize_file_1:
    List.append(int(line))
import itertools

for pair in itertools.combinations(List,2):
    
    if sum(pair) >9:
        
        print (pair)
