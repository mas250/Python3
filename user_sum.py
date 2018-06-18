user_sum = input("keep entering numbers, end with q or Q: ")
total = []
while user_sum != 'q':
    
    total.append(int(user_sum))    
    user_sum = input("keep entering numbers, end with q or Q: ")
    

    

    
print(sum(total)/len(total))
