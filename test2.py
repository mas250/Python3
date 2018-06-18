prize_file_1 = open("/Users/MatBook/Downloads/prize1.txt")
List = []
prizes = []
for line in prize_file_1:
    List.append(int(line))
    
first_line = List.pop(0)

for i in List:
    largest = i
    if i + largest == 10:
        largest = i
print(largest)
            
            
    




print (List)
print( "you can have:", prizes)
