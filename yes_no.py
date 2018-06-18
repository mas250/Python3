user_anwser = input("keep entering responses: ")
user_list = []
while user_anwser != 'y' or 'yes' or 'Y' or 'YES' or 'n' or 'N' or 'NO' or 'no':
    
   
    if user_anwser > 0:
        user_list.append(user_anwser)
        user_anwser = input("keep entering numbers, end with q or Q: ")
                         
    else:
        
        user_list.insert(0,user_anwser)
        user_anwser = input("keep entering numbers, end with q or Q: ")                       

else:
    print (total)

    

