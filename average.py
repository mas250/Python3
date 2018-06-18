


def get_num():
    count = 0
    user_average = 0
    
    while True:
        
        try:
            user_int = float(input("type a number, q to stop: "))
            if user_int == 'q':
                print (user_average)
                break
            user_int += user_int
            count +=1
        
            user_average = user_int / count
            
        except:
            print("error found")
            print (user_average)
            break
        
                
get_num()
