H = [12.5, 6.4, 10, 7.6, 8, 13]
x = range(6)

def historgam(x,y,width= 30):
    '''prints a histogram where the highest value has 30 stars '''
    stars = 0
    for i in y:
        maxvalue = max(H)               #find the largest value in the list
        count = 0
        assert len (x) == len(H)
        
    for i in H:
        stars = (i*width)/maxvalue      #get the ratio for the amount of stars to print
        stars = '*' * int(stars)
        print(x[count],stars,i)         
        count = count+1
    
historgam(x,H,width= 30)
