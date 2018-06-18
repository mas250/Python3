prize_file_1 = open("/Users/MatBook/Downloads/prize3.txt")
List = []
prizes = []
for line in prize_file_1:
    List.append(int(line))
    
first_line = List.pop(0)

for i in List:
    print(i)
  
    for j in List:
        if i + j == first_line:
            prizes.append((i,j))

        
            

    




print (List)
print( "you can have:", prizes)
